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

from .OutputTrigger import OutputTrigger


class OutputTriggerTime(pyre.component, implements=OutputTrigger, family="pylith.observers.output_triggers.time"):
    """Trigger output based on time step index."""

    elapsed_time = pylith.properties.dimensional(default=0 * year)
    elapsed_time.validators = pyre.constraints.isGreaterEqual(value=0 * year)
    elapsed_time.doc = "Elasped time between writes."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement OutputTriggerStep.__init__(). Pass parameters to C++.",
                f"elapsed time={self.elapsed_time}",
            )
        )
        todo.log()
