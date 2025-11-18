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

from pylith.solvers import solver
from pylith.boundary_conditions import boundary_condition
from pylith.initial_conditions import initial_condition
from pylith.observers import solution_domain


class GoverningEqn(pylith.protocol, family="pylith.governing_eqns"):
    """Protocol declarator for governing equations." """

    @classmethod
    def pyre_default(cls, **kwds):
        """
        The default {GoverningEqn} implementation
        """
        from .Elasticity import Elasticity

        return Elasticity


class GoverningEqnBase(pylith.component, implements=GoverningEqn):

    solver = solver()
    solver.doc = "Solver for governing equation."

    boundary_conditions = pylith.properties.list(schema=boundary_condition())
    boundary_conditions.doc = "Boundary conditions."

    initial_conditions = pylith.properties.list(schema=initial_condition())
    initial_conditions.doc = "Boundary conditions."

    observers = pylith.properties.list(schema=solution_domain())
    observers.doc = "Observers of solution to governing equation."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement GoverningEqn.__init__(). Pass parameters to C++.",
                f"solver={self.solver}",
                f"boundary conditions={self.boundary_conditions}",
                f"initial conditions={self.initial_conditions}",
                f"observers={self.observers}",
            )
        )
        todo.log()
