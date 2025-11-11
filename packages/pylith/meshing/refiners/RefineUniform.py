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
from pylith import journal

from .Refiner import Refiner


class RefineUniform(pylith.component, implements=Refiner, family="pylith.meshing.refiners.uniform"):

    levels = pylith.properties.int(default=0)
    levels.validators = pyre.constraints.isGreaterEqual(value=0)
    levels.doc = "Number of refinement levels."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement RefineUniform.__init__(). Pass parameters to C++.",
                f"levels={self.levels}",
            )
        )
        todo.log()
