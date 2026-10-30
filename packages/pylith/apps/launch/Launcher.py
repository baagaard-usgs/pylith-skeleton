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

from .Job import Job
from .exceptions import JobRunningError


class Launcher:
    """The interface a launch backend presents to the GraphQL layer.

    A backend starts a configured simulation, tracks the one job it is running, and cancels
    it on request. The local backend ({LocalLauncher}) runs the job as a child of the web
    server; a future SLURM-over-SSH backend would submit it to a batch queue. Both present
    the same {start}, {cancel}, and {current} to the resolvers, so the GraphQL contract does
    not change when the second backend lands.

    The server holds one launcher, which holds one job at a time: this is a single-user,
    local GUI, with no per-client job ownership.
    """

    def start(self):
        """Start the configured simulation and return its {Job} record.

        A backend that already has a job RUNNING raises {JobRunningError}, which the GraphQL
        handler turns into an error document; a new run otherwise replaces the record of the
        last one. Subclasses implement this.
        """
        # the interface does not run anything itself
        raise NotImplementedError(f"class '{type(self).__name__}' must implement 'start'")

    def cancel(self, id):
        """Cancel the job named {id} and return its {Job} record.

        A request for a job that is not the current running one, or when nothing is running,
        returns the current record unchanged. Subclasses implement this.
        """
        # the interface does not cancel anything itself
        raise NotImplementedError(f"class '{type(self).__name__}' must implement 'cancel'")

    def current(self):
        """Return the current {Job} record, or the IDLE sentinel if none has run.

        The default reports whatever {_job} holds, falling back to the sentinel; a backend
        that tracks its job elsewhere overrides this.
        """
        # the job on record, or the sentinel when there is none
        return self._job if self._job is not None else Job.idle()

    # metamethods
    def __init__(self, **kwds):
        super().__init__(**kwds)
        # the one job the launcher tracks; {None} until the first run
        self._job = None
        # all done
        return

    # the exception a double start raises, published so resolvers can name it
    JobRunningError = JobRunningError


# End of file
