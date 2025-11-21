# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================

import pylith

from ...meshing import refiners
from .InitializePhase import InitializePhase


class MeshRefiner(pylith.component, implements=InitializePhase, family="pylith.mesh_initializers.phases.refiner"):

    refiner = refiners.refiner(default=refiners.uniform)
    refiner.doc = "Refine finite-element mesh."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"refiner = {self.refiner}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement MeshRefiner.__init__(). Pass parameters to C++.",))
        todo.log()
