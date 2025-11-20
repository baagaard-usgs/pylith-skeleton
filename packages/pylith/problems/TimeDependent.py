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
from pyre.units.time import second

import pylith

from .. import protocols
from .. import monitors

from .ProblemBase import ProblemBase


class TimeDependent(ProblemBase, family="pylith.problems.time_dependent"):
    """A time dependent problem."""

    start_time = pylith.properties.dimensional(default=0.0 * second)
    start_time.doc = "Problem start time."

    end_time = pylith.properties.dimensional(default=0.0 * second)
    end_time.doc = "Problem end time."

    initial_time_step = pylith.properties.dimensional(default=1.0 * second)
    initial_time_step.validators = pyre.constraints.isGreater(value=0.0 * second)
    initial_time_step.doc = "Initial time step for solve."

    max_time_steps = pylith.properties.int(default=20000)
    max_time_steps.validators = pyre.constraints.isPositive()
    max_time_steps.doc = "Maximum number of time steps."

    progress_monitor = protocols.progress_monitor(default=monitors.progress_monitor_time)
    progress_monitor.doc = "Monitor for reporting progress of simulation."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        # self.cxx = CxxTimeDependent()
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement TimeDependent.__init__(). Pass parameters to C++.",
                f"start time={self.start_time}",
                f"end time={self.end_time}",
                f"initial time step={self.initial_time_step}",
                f"maximum number of time steps={self.max_time_steps}",
                f"progress monitor={self.progress_monitor}",
            )
        )
        todo.log()
