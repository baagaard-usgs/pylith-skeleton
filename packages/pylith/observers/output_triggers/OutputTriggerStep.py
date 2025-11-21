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

from ...protocols.observers import output_trigger


class OutputTriggerStep(pyre.component, implements=output_trigger, family="pylith.observers.output_triggers.step"):
    """Trigger output based on time step index."""

    num_skip = pylith.properties.int(default=0)
    num_skip.validators = pyre.constraints.isGreaterEqual(value=0)
    num_skip.doc = "Number of solution steps to skip between writes (0 means write every time step)."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"num skip = {self.num_skip}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement OutputTriggerStep.__init__(). Pass parameters to C++.",))
        todo.log()
