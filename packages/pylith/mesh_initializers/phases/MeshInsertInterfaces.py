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

from .InitializePhase import InitializePhase


class MeshInsertInterfaces(
    pylith.component, implements=InitializePhase, family="pylith.mesh_initializers.phases.insert_interfaces"
):

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement MeshInsertInterfaces.__init__().",
            )
        )
        todo.log()
