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


class OptionsManager(pyre.component, implements=Options, family="pylith.petsc.options.manager"):
    """Default parameters for simulation."""

    options = pylith.properties.list(schema=pylith.properties.tuple(schema=pylith.properties.str()))
    options.doc = "List of PETSc options as tuples."

    collective_io = pylith.properties.bool(default=True)
    collective_io.doc = "Use default PETSc collective I/O options."

    testing = pylith.properties.bool(default=False)
    testing.doc = "Use default PETSc testing options."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        if self.collective_io:
            pyre.loadConfiguration("petsc-collective-io.yaml")
        if self.testing:
            pyre.loadConfiguration("petsc-testing.yaml")

        todo = journal.warning(":TODO:")
        todo.report(
            (
                "Implement SimulationDefaults.__init__(). Pass parameters to C++.",
                f"options={self.options}",
                f"collective_io={self.collective_io}",
                f"testing={self.testing}",
            )
        )
        todo.log()
