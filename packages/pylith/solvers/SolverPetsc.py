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
from pylith.petsc.options import groups

from .Solver import Solver


class SolverPetsc(pyre.component, implements=Solver, family="pylith.solvers.petsc"):
    """PETSc solver."""

    formulation = pylith.properties.str(default="implicit")
    formulation.validators = pyre.constraints.isMember("implicit", "explicit", "implicit_explicit")
    formulation.doc = "Formulation for solver."

    # :TODO: Convert to dict or just use names?
    petsc_options = pylith.properties.list(schema=groups.group())
    petsc_options.doc = "Groups of solver related PETSc options."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement SolverPetsc.__init__(). Pass parameters to C++.",
                f"formulation={self.formulation}",
                f"PETSc options={self.petsc_options}",
            )
        )
        todo.log()
