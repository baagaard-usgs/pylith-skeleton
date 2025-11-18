# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import pyre

import pylith


class ProgressMonitor(pylith.protocol, family="pylith.monitors"):
    """Protocol declarator for defaults." """

    @classmethod
    def pyre_default(cls, **kwds):
        """
        The default {ProgressMonitor} implementation
        """
        from .ProgressMonitorTime import ProgressMonitorTime

        return ProgressMonitorTime


class ProgressMonitorBase(pylith.component, implements=ProgressMonitor):
    """Abstract base class for simulation progress monitors."""

    filename = pylith.properties.str()
    filename.doc = "Name of output file."

    update_percent = pylith.properties.float(default=5.0)
    update_percent.validators = pyre.constraints.isPositive()
    update_percent.doc = "Frequency of progress updates (percent)."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                "Implement ProgressMonitorBase.__init__(). Pass parameters to C++.",
                f"filename={self.filename}",
                f"update percent={self.update_percent}",
            )
        )
        todo.log()
