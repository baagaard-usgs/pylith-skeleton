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
from pyre.units.time import year

import pylith

from .ProgressMonitor import ProgressMonitorBase


class ProgressMonitorTime(ProgressMonitorBase, family="pylith.monitors.progress_monitor_time"):
    """Monitor progress of a time-dependent simulation."""

    time_units = pylith.properties.dimensional(default=1.0 * year)
    time_units.validators = pyre.constraints.isGreater(value=0.0 * year)
    time_units.doc = "Units used for simulation time in output."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement ProgressMonitorTime.__init__(). Pass parameters to C++.",
                f"time units={self.time_units}",
            )
        )
        todo.log()
