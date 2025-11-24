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

from ...protocols import mesh_initializers


class MeshDistributor(
    pylith.component,
    implements=mesh_initializers.initialize_phase,
    family="pylith.mesh_initializers.phases.distributor",
):

    distributor = mesh_initializers.distributor()
    distributor.doc = "Mesh partitioner and distributor."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"distributor = {self.distributor}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement MeshDistributor.__init__(). Pass parameters to C++.",))
        todo.log()
