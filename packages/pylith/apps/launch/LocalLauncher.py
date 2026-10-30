# -*- Python -*-
# -*- coding: utf-8 -*-
#
# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2026, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================

import functools
import json
import os
import signal
import subprocess

import journal
from pyre.ipc.Pipe import Pipe
from pyre.units.SI import second

import pylith

from .Job import Job
from .Launcher import Launcher


class LocalLauncher(Launcher):
    """Run a configured simulation as a child of the web server.

    A start spawns {pylith run} with the server's own environment and working directory, so
    the child resolves the same configuration the server read, the local equivalent of the
    {run} subcommand. The child runs alongside the server rather than inside it: its output
    pipes are watched on the server's event loop, its lines are re-logged into the server
    journal so they ride the journal stream the Monitor already renders, and it is reaped
    through a {SIGCHLD} handler, so the server keeps answering requests while the job runs.

    The launcher holds one job at a time (single-user, local GUI). A start while a job is
    RUNNING is refused; a start after a job has ended replaces the record.
    """

    # constants
    # the hub topic the job-state frames ride on; the journal stream the client already
    # watches, so a state change reaches the browser without a second connection
    topic = "journal"
    # the frame name, so the client can tell a job-state frame from a batch of journal records
    event = "job"
    # the journal channels the child's output is re-logged through, so the Monitor selector
    # offers them like any other channel
    stdoutChannel = "stdout"
    stderrChannel = "stderr"
    # how long a cancelled child is given to exit on {SIGTERM} before it is sent {SIGKILL}
    grace = 5 * second

    # interface
    def start(self):
        """Spawn {pylith run} and return the RUNNING job record.

        Refuses, by raising {JobRunningError}, if a job is already running.
        """
        # the job on record
        job = self._job
        # if one is running
        if job is not None and job.state == "RUNNING":
            # refuse; the GraphQL handler turns this into an error document
            raise self.JobRunningError(id=job.id)

        # build the command that reproduces a CLI {pylith run}
        command = self._command()
        # spawn the child with its output on pipes we can watch
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            # the server's own environment and working directory, so the child resolves the
            # same configuration files the server read
            cwd=os.getcwd(),
            env=os.environ,
        )
        # record the job
        job = Job(
            id=f"job:{process.pid}",
            state="RUNNING",
            command=" ".join(command),
            pid=process.pid,
            started_at=Job.now(),
        )
        # remember it and the child that backs it
        self._job = job
        self._process = process
        # watch the child's output on the event loop, re-logging each line into the journal
        self._watch(stream=process.stdout, sink=self.stdoutChannel, pid=process.pid)
        self._watch(stream=process.stderr, sink=self.stderrChannel, pid=process.pid)
        # make sure the child is reaped when it exits
        self._arm()
        # tell the client the job has started
        self._announce(job=job)
        # hand back the record
        return job

    def cancel(self, id):
        """Stop the job named {id} and return its record.

        A request for a job that is not the one running, or when nothing is running, returns
        the current record unchanged.
        """
        # the job on record
        job = self._job
        # if nothing is running, or this is not the running job, there is nothing to do
        if job is None or job.state != "RUNNING" or job.id != id:
            # report whatever is on record
            return self.current()
        # ask the child to stop
        try:
            # politely first
            os.kill(job.pid, signal.SIGTERM)
        # tolerating a child that has already gone
        except ProcessLookupError:
            # the reaper will record its terminal state
            pass
        # remember that this stop was a cancellation, so the reaper records CANCELLED rather
        # than reading the exit code as a failure
        self._cancelling = job.pid
        # escalate to {SIGKILL} if it has not exited by the time the grace period lapses
        self._server.dispatcher.alarm(interval=self.grace, call=self._escalate)
        # report the record; its terminal state follows on the job-state frame when it exits
        return job

    def current(self):
        """Return the current job record, or the IDLE sentinel if none has run."""
        # the job on record, or the sentinel when there is none
        return self._job if self._job is not None else Job.idle()

    # metamethods
    def __init__(self, server, **kwds):
        super().__init__(**kwds)
        # the server whose event loop, hub, and stream framing the launcher uses
        self._server = server
        # the child that backs the running job, if any
        self._process = None
        # the pid of a child that is being cancelled, so the reaper can tell a cancel from a
        # failure; {None} when no cancel is pending
        self._cancelling = None
        # whether the {SIGCHLD} handler is armed
        self._armed = False
        # the per-descriptor carry-over buffers for partial lines
        self._buffers = {}
        # all done
        return

    # implementation details
    def _command(self):
        """Build the {pylith run} command line the child runs."""
        # the executable is the {pylith} entry point on the install {bin}, the one that
        # started the server, so {run} in the child resolves the same configuration
        executable = pylith.prefix / "bin" / "pylith"
        # invoked with the {run} action
        return [str(executable), "run"]

    def _watch(self, stream, sink, pid):
        """Watch {stream} on the event loop, re-logging each line it carries to the journal.

        The child's output rides the server journal so it reaches the Monitor stream; each
        line is logged on the journal channel named by {sink} and stamped with the child
        {pid}, so the Monitor can tell the child's records from the server's own.
        """
        # the raw descriptor behind the stream
        fd = stream.fileno()
        # a non-blocking read, so the handler never stalls the loop when a line is partway in
        os.set_blocking(fd, False)
        # wrap the raw descriptor as a channel the dispatcher can watch
        pipe = Pipe(infd=fd, outfd=fd)
        # start its carry-over buffer empty
        self._buffers[fd] = b""
        # register the reader; the handler works from the descriptor, journal channel, and pid
        # bound here, and ignores the {channel} the dispatcher passes, which names the pipe,
        # not the journal channel, and must not be confused with {sink}
        self._server.dispatcher.whenReadReady(
            channel=pipe,
            call=functools.partial(self._drain, fd=fd, pipe=pipe, sink=sink, pid=pid),
        )
        # all done
        return

    def _drain(self, fd, pipe, sink, pid, **kwds):
        """Read what is available on {fd}, log whole lines, and report whether to keep watching.

        Returns {True} while the pipe is open, so the dispatcher reschedules the reader, and a
        falsy value at end of stream, so it is released. This is a read-readiness handler; the
        dispatcher passes the pipe it watched as the {channel} keyword, which this handler
        does not need and absorbs through {kwds}.
        """
        # read what is available
        try:
            # an empty read means the child closed this end
            chunk = os.read(fd, 64 * 1024)
        # a descriptor that was closed behind our back, e.g. when the child was reaped and its
        # pipes released, reads as end of stream rather than an error that stalls the loop
        except OSError:
            # treat it as the end
            chunk = b""
        # if the stream is at its end
        if not chunk:
            # flush any partial line left in the buffer as a record of its own
            self._flush(fd=fd, sink=sink, pid=pid)
            # stop watching this descriptor, so its number can be recycled safely
            self._server.dispatcher.forget(channel=pipe)
            # release the reader
            return False
        # otherwise, append to the carry-over buffer
        data = self._buffers[fd] + chunk
        # split into whole lines, keeping any trailing partial for the next read
        *lines, self._buffers[fd] = data.split(b"\n")
        # re-log each whole line
        for line in lines:
            # through the journal channel the child's output rides on
            self._log(sink=sink, pid=pid, text=line.decode("utf-8", "replace"))
        # keep watching
        return True

    def _flush(self, fd, sink, pid):
        """Log the partial line left in {fd}'s buffer at end of stream, if any."""
        # the carry-over buffer
        data = self._buffers.pop(fd, b"")
        # if there is a partial line
        if data:
            # log it as its own record
            self._log(sink=sink, pid=pid, text=data.decode("utf-8", "replace"))
        # all done
        return

    def _log(self, sink, pid, text):
        """Re-log one line of the child's output through the {sink} journal channel.

        Stdout rides an {info} channel and stderr an {error} channel; the line is stamped with
        the child {pid} so the Monitor can attribute it to the child rather than the server.
        """
        # open the channel; stderr goes to an error channel, everything else to info
        factory = journal.error if sink == self.stderrChannel else journal.info
        # the channel speaks under the name the child's stream maps to
        entry = factory(sink)
        # an error channel that aborts would take the server down, so it must not here
        entry.fatal = False
        # record the line, stamping the child pid so the device keeps it as the origin
        entry.log(text, pid=pid)
        # all done
        return

    def _arm(self):
        """Register the {SIGCHLD} reaper on the event loop, once."""
        # if it is already armed
        if self._armed:
            # nothing to do
            return
        # ask the dispatcher to call the reaper when a child changes state
        self._server.dispatcher.whenSignal(signal=signal.SIGCHLD, call=self._reap)
        # and remember
        self._armed = True
        # all done
        return

    def _reap(self, **kwds):
        """Reap the exited child and record the job's terminal state.

        This is a {SIGCHLD} handler; returning {True} keeps it registered for the next run.
        The reaping goes through {Popen.poll}, which does a non-blocking wait and caches the
        return code, so the child is reaped exactly once and the subprocess bookkeeping stays
        consistent.
        """
        # the child that backs the running job
        process = self._process
        # if there is none, or the job is no longer running, there is nothing to reap
        if process is None or self._job is None or self._job.state != "RUNNING":
            # stay registered for a later run
            return True
        # ask whether the child has exited, without blocking
        code = process.poll()
        # if it is still running
        if code is None:
            # wait for the next signal
            return True
        # the child is gone; {poll} has reaped it and cached the return code, which is already
        # the exit code, negative for a signal that killed it
        self._settle(code=code)
        # stay registered for a later run
        return True

    def _settle(self, code):
        """Record the terminal state and exit code of the job that just ended."""
        # the job on record
        job = self._job
        # if this end was a cancellation
        if self._cancelling == job.pid:
            # the run was cancelled; the exit code is not meaningful
            state, exitCode = "CANCELLED", None
            # the cancellation is resolved
            self._cancelling = None
        # otherwise a clean exit succeeds
        elif code == 0:
            state, exitCode = "SUCCEEDED", 0
        # and any other exit fails
        else:
            state, exitCode = "FAILED", code
        # build the terminal record, carrying the identity and command forward
        job = Job(
            id=job.id,
            state=state,
            command=job.command,
            pid=job.pid,
            started_at=job.started_at,
            exit_code=exitCode,
        )
        # put it on record
        self._job = job
        # and tell the client
        self._announce(job=job)
        # all done
        return

    def _escalate(self, timestamp, **kwds):
        """Send {SIGKILL} to a cancelled child that has not exited on {SIGTERM}.

        This is an alarm handler; returning {None} keeps it from being rescheduled.
        """
        # the child that backs the running job
        process = self._process
        # if it is already gone, or there is no cancel pending, there is nothing to do
        if process is None or self._cancelling is None:
            # do not reschedule
            return None
        # otherwise end it with prejudice
        try:
            # it has had its grace period
            os.kill(process.pid, signal.SIGKILL)
        # tolerating one that has gone on its own in the meantime
        except ProcessLookupError:
            # nothing further
            pass
        # do not reschedule
        return None

    def _announce(self, job):
        """Publish a job-state frame so the client learns of a state change.

        The frame rides the journal topic the client already watches, under the {job} event
        name, so the client folds the new state in without polling and without a second
        connection.
        """
        # the server whose hub carries the frame
        server = self._server
        # the job as a wire object
        payload = json.dumps(self._raw(job=job), ensure_ascii=False)
        # a stream, for the framing
        stream = server.eventStream(server=server)
        # frame the payload under my event name
        frame = stream.event(payload, name=self.event)
        # publish it to the journal subscribers
        server.hub.publish(frame, topic=self.topic)
        # all done
        return

    @staticmethod
    def _raw(job):
        """Render {job} as the wire object the client's job-state frame carries."""
        # the fields the client reads, named as the GraphQL {Job} type exposes them
        return {
            "id": job.id,
            "state": job.state,
            "command": job.command,
            "startedAt": job.started_at,
            "exitCode": job.exit_code,
        }


# End of file
