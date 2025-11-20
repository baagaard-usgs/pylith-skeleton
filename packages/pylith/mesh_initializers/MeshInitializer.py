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

from ..protocols import mesh_initializer
from ..protocols.mesh_initializers import initialize_phase


class MeshInitializer(
    pylith.component, implements=mesh_initializer, family="pylith.mesh_initializers.mesh_initializer"
):

    phases = pylith.properties.list(schema=initialize_phase())
    phases.doc = "Phases for mesh initialization."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        lines = [
            f"{self}",
            "Implement MeshInitializer.__init__(). Pass parameters to C++.",
            "Phases:",
        ]
        lines += [f"   {phase}" for phase in self.phases]
        todo.report(lines)
        todo.log()
