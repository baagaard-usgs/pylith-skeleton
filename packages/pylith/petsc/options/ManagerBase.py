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

from ...protocols.petsc import options_manager


class ManagerBase(pylith.component, implements=options_manager):
    """Abstract base class for PETSc options managers."""

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        lines = [
            "Implement ManagerBase.__init__(). Pass parameters to C++.",
            f"{self}",
            "Option sections:",
        ]
        lines += [f"    - {trait}" for trait in self.pyre_traits()]
        info.report(lines)
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement ManagerBase.__init__(). Pass parameters to C++.",))
        todo.log()
