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

from .Options import Options


class ManagerBase(pylith.component, implements=Options):
    """Abstract base class for PETSc options managers."""

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        lines = [
            f"{self}",
            "Implement OptionsManager.__init__(). Pass parameters to C++.",
            "Option sections:",
        ]
        lines += [f"    {trait}" for trait in self.pyre_traits()]
        todo.report(lines)
        todo.log()
