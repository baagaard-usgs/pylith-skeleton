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

        info = pylith.journal.info_factory.initialization()
        lines = [
            f"{self}",
            "Phases:",
        ]
        lines += [f"    - {phase}" for phase in self.phases]
        info.report(lines)
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(
            "Implement MeshInitializer.__init__(). Pass parameters to C++.",
        )
        todo.log()
