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

from pylith import mesh_io
from .InitializePhase import InitializePhase


class MeshWriter(pylith.component, implements=InitializePhase, family="pylith.mesh_initializers.phases.writer"):

    writer = mesh_io.mesh_io(default=mesh_io.petsc)
    writer.doc = "Mesh writer."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement MeshWriter.__init__(). Pass parameters to C++.",
                f"writer={self.writer}",
            )
        )
        todo.log()
