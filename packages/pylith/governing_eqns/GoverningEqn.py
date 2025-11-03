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

from pylith.solvers import solver
from pylith.fields import field
from pylith.boundary_conditions import boundary_condition
from pylith.initial_conditions import initial_condition
from pylith.observers import solution_domain


class GoverningEqn(pylith.protocol, family="pylith.governing_eqns"):
    """Protocol declarator for governing equations." """

    @classmethod
    def pyre_default(cls, **kwds):
        """
        The default {Defaults} implementation
        """
        from .Elasticity import Elasticity

        return Elasticity


class GoverningEqnBase(pylith.component, implements=GoverningEqn):

    solver = solver()
    solver.doc = "Solver for elasticity equation."

    solution = field()
    solution.doc = "Solution field for elasticity equation."

    boundary_conditions = pylith.properties.list(schema=boundary_condition())
    boundary_conditions.doc = "Boundary conditions."

    initial_conditions = pylith.properties.list(schema=initial_condition())
    initial_conditions.doc = "Boundary conditions."

    observers = pylith.properties.list(schema=solution_domain())
    observers.doc = "Observers of solution to governing equation."
