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

from .. import protocols
from ..protocols.mesh_initializers import distributor
from ..protocols.meshing import refiner, interfaces

from .. import mesh_io
from ..meshing import refiners, insert_interfaces
from . import distributors


class InitializerParallel(
    pylith.component, implements=protocols.mesh_initializer, family="pylith.mesh_initializers.parallel"
):

    read_mesh = protocols.mesh_io(default=mesh_io.petsc)
    read_mesh.doc = "Read mesh in parallel."

    distribute_mesh = distributor(default=distributors.petsc)
    distribute_mesh.doc = "Distribute mesh."

    insert_interfaces = interfaces(default=insert_interfaces.create_cohesive_cells)
    insert_interfaces.doc = "Insert interior interfaces."

    refine_mesh = refiner(default=refiners.uniform)
    refine_mesh.doc = "Refine mesh."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"read mesh = {self.read_mesh}",
                f"distribute mesh = {self.distribute_mesh}",
                f"insert interfaces = {self.insert_interfaces}",
                f"refine mesh = {self.refine_mesh}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(
            "Implement InitializerParallel.__init__(). Pass parameters to C++.",
        )
        todo.log()
