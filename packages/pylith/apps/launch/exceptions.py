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


class LaunchError(Exception):
    """The base of the errors a launch backend raises."""


class JobRunningError(LaunchError):
    """A start was requested while a job was already running.

    The server holds one job at a time, so a second start is refused rather than silently
    replacing a live run. The GraphQL handler turns this into an error document the client
    surfaces; in normal use the client keeps the Run control disabled while a job runs, so
    the condition is unreachable.
    """

    def __init__(self, id, **kwds):
        # assemble the report naming the job that is in the way
        reason = f"a job ('{id}') is already running"
        super().__init__(reason, **kwds)
        # remember the offending job's identity
        self.id = id
        # all done
        return


# End of file
