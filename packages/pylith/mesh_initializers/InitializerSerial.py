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
from ..protocols.mesh_initializers import initialize_phase

from . import phases


class InitializerSerial(
    pylith.component, implements=protocols.mesh_initializer, family="pylith.mesh_initializers.serial"
):

    read_mesh = initialize_phase(default=phases.reader)
    read_mesh.doc = "Read mesh."

    reorder_mesh = initialize_phase(default=phases.reordering)
    reorder_mesh.doc = "Reorder mesh."

    distribute_mesh = initialize_phase(default=phases.distributor)
    distribute_mesh.doc = "Distribute mesh."

    insert_interfaces = initialize_phase(default=phases.insert_interfaces)
    insert_interfaces.doc = "Insert interior interfaces."

    refine_mesh = initialize_phase(default=phases.refiner)
    refine_mesh.doc = "Refine mesh."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"read mesh = {self.read_mesh}",
                f"reorder mesh = {self.reorder_mesh}",
                f"distribute mesh = {self.distribute_mesh}",
                f"insert interfaces = {self.insert_interfaces}",
                f"refine mesh = {self.refine_mesh}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(
            "Implement MeshInitializer.__init__(). Pass parameters to C++.",
        )
        todo.log()
