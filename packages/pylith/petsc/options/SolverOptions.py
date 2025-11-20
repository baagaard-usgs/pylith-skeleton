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

from .ManagerBase import ManagerBase

from ...protocols.petsc import options


class SolverOptions(ManagerBase, family="pylith.petsc.options.solver"):
    """PETSc options manager for solver options."""

    solver = options.group()
    solver.doc = "Options for solving the equations."

    initial_guess = options.group()
    initial_guess.doc = "Options for setting an initial guess."

    tolerances = options.group()
    tolerances.doc = "Solver tolerances."

    adaptive_ts = options.group()
    adaptive_ts.doc = "Options for adaptive time stepping."

    monitoring = options.group()
    monitoring.doc = "Options for monitoring the solver."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement SolverOptions.__init__(). Pass parameters to C++.",
            )
        )
        todo.log()
