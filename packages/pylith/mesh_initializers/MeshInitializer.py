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
from .phases.InitializePhase import InitializePhase
from .phases.MeshReader import MeshReader

from .Initializer import Initializer


class MeshInitializer(pylith.component, implements=Initializer, family="pylith.mesh_initializers.mesh_initializer"):

    phases = pylith.properties.list(schema=InitializePhase(default=MeshReader))
    phases.doc = "Phases for mesh initialization."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        self.phases

        todo = journal.warning(":TODO:")
        lines = [
            "Implement MeshInitializer.__init__(). Pass parameters to C++.",
            f"Phases={self.phases}",
        ]
        lines += [f"   {phase}" for phase in self.phases]
        todo.report(lines)
        todo.log()
