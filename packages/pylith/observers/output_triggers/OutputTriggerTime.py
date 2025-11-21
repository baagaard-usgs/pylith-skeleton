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

from ...protocols.observers import output_trigger


class OutputTriggerTime(pyre.component, implements=output_trigger, family="pylith.observers.output_triggers.time"):
    """Trigger output based on time step index."""

    elapsed_time = pylith.properties.dimensional(default=0 * year)
    elapsed_time.validators = pyre.constraints.isGreaterEqual(value=0 * year)
    elapsed_time.doc = "Elasped time between writes."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"elapsed time={self.elapsed_time}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement OutputTriggerStep.__init__(). Pass parameters to C++.",))
        todo.log()
