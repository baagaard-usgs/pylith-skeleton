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

from .Options import Options
from .groups import group


class OptionsManager(pyre.component, implements=Options, family="pylith.petsc.options"):
    """PETSc options manager."""

    # :TODO: Convert to dict or just use names?
    groups = pylith.properties.list(schema=group())
    groups.doc = "List of groups of PETSc options."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        self.groups

        todo = journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement OptionsManager.__init__(). Pass parameters to C++.",
                f"groups={self.groups}",
            )
        )
        todo.log()
