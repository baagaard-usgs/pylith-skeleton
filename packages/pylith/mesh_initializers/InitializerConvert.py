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
from ..protocols.mesh_initializers import reordering

from .. import mesh_io
from . import reorderings


class InitializerConvert(
    pylith.component, implements=protocols.mesh_initializer, family="pylith.mesh_initializers.convert"
):

    read_mesh = protocols.mesh_io(default=mesh_io.petsc)
    read_mesh.doc = "Read mesh in serial."

    reorder_mesh = reordering(default=reorderings.petsc)
    reorder_mesh.doc = "Reorder mesh."

    write_mesh = protocols.mesh_io(default=mesh_io.petsc)
    write_mesh.doc = "Write mesh."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"read mesh = {self.read_mesh}",
                f"reorder mesh = {self.reorder_mesh}",
                f"write mesh = {self.write_mesh}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(
            "Implement InitializerConvert.__init__(). Pass parameters to C++.",
        )
        todo.log()
