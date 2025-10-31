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
from pylith import solvers
from pylith import solutions
from pylith import materials
from pylith import interior_interfaces

from .GoverningEqn import GoverningEqn


class Elasticity(GoverningEqn, family="pylith.governing_eqns.elasticity"):
    """Elasticity governing equation."""

    solver = solvers.solver(default=solvers.petsc_solver)
    solver.doc = "Solver for elasticity equation."

    solution = solutions.solution(default=solutions.elasticity)
    solution.doc = "Solution field for elasticity equation."

    materials = pylith.properties.list(schema=materials.material(default=materials.elasticity))
    materials.doc = "Materials in boundary value problem."

    interior_interfaces = pylith.properties.list(schema=interfaces.interface(default=interfaces.elasticity))
    interior_interfaces.doc = "Interior interfaces (faults) in boundary value problem."

    # - gravity_field

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        if len(self.interior_interfaces):
            pyre.loadConfiguration("solver-elasticity-fault.yaml")
            pyre.loadConfiguration("solution-elasticity-fault.yaml")
        else:
            pyre.loadConfiguration("solver-elasticity.yaml")
            pyre.loadConfiguration("solution-elasticity.yaml")

        todo = journal.warning(":TODO:")
        todo.report(
            (
                "Implement Elasticity.__init__(). Pass parameters to C++.",
                f"solver={self.solver}",
                f"solution={self.solution``}",
                f"materials={self.materials}",
                f"interior interfaces={self.interior_interfaces}",
            )
        )
        todo.log()
