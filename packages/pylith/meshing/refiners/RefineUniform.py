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

from ...protocols import meshing


class RefineUniform(pylith.component, implements=meshing.refiner, family="pylith.meshing.refiners.uniform"):

    levels = pylith.properties.int(default=0)
    levels.validators = pyre.constraints.isGreaterEqual(value=0)
    levels.doc = "Number of refinement levels."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"levels={self.levels}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement RefineUniform.__init__(). Pass parameters to C++.",))
        todo.log()
