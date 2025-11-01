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
from pylith import journal

from pylith.mesh_initializers import distributors
from .InitializePhase import InitializePhase


class MeshDistributor(
    pylith.component, implements=InitializePhase, family="pylith.mesh_initializers.phases.distributor"
):

    distributor = distributors.distributor(default=distributors.petsc)
    distributor.doc = "Mesh partitioner and distributor."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.warning(":TODO:")
        todo.report(
            (
                "Implement MeshDistributor.__init__(). Pass parameters to C++.",
                f"distributor={self.distributor}",
            )
        )
        todo.log()
