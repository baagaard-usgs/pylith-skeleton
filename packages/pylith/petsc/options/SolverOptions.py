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

from . import groups


class SolverOptions(ManagerBase, family="pylith.petsc.options.solver"):
    """PETSc options manager for solver options."""

    solver = groups.group(default=groups.group_list)
    solver.doc = "Options for solving the equations."

    initial_guess = groups.group(default=groups.group_list)
    initial_guess.doc = "Options for setting an initial guess."

    tolerances = groups.group(default=groups.group_list)
    tolerances.doc = "Solver tolerances."

    adaptive_ts = groups.group(default=groups.group_list)
    adaptive_ts.doc = "Options for adaptive time stepping."

    monitoring = groups.group(default=groups.group_list)
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
