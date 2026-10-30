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

import datetime

# the set of states a job passes through, scheduler-agnostic so a local run and a future
# SLURM submission present the same shape to the UI
states = frozenset({"IDLE", "RUNNING", "SUCCEEDED", "FAILED", "CANCELLED"})


class Job:
    """The record of one launched simulation, as the UI sees it.

    The record is scheduler-agnostic: the local launcher and a future SLURM backend fill in
    the same fields, so the GraphQL {Job} type and the client need not know which backend
    produced it. An idle launcher hands back the {idle} sentinel rather than {None}, so the
    {job} query always has something to resolve.
    """

    def __init__(self, *, id, state, command=None, pid=None, started_at=None, exit_code=None, **kwds):
        super().__init__(**kwds)
        # a stable identity the client folds the record into its store by
        self.id = id
        # one of {states}
        self.state = state
        # the command line that was run, or {None} while idle
        self.command = command
        # the process id of the child, while it is known
        self.pid = pid
        # when the run started, as an ISO-8601 string, or {None} while idle
        self.started_at = started_at
        # the exit code once the run ends, or {None} while it runs and for a cancelled run
        self.exit_code = exit_code
        # all done
        return

    @classmethod
    def idle(cls):
        """Build the sentinel the launcher reports before any job has run."""
        # a record in the IDLE state with nothing else filled in
        return cls(id="job:idle", state="IDLE")

    @staticmethod
    def now():
        """Return the current time as an ISO-8601 string, for the {started_at} field."""
        # the local time, to the second
        return datetime.datetime.now().replace(microsecond=0).isoformat()


# End of file
