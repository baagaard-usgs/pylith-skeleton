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

from .OptionsManagerBase import OptionsManagerBase

from ...protocols.petsc.options import groups
from .groups import group_list


class SolverOptions(OptionsManagerBase, family="pylith.petsc.options.solver_options"):
    """PETSc options manager for solver options."""

    solver = groups.group(default=group_list)
    solver.doc = "Options for solving the equations."

    initial_guess = groups.group(default=group_list)
    initial_guess.doc = "Options for setting an initial guess."

    tolerances = groups.group(default=group_list)
    tolerances.doc = "Solver tolerances."

    adaptive_ts = groups.group(default=group_list)
    adaptive_ts.doc = "Options for adaptive time stepping."

    monitoring = groups.group(default=group_list)
    monitoring.doc = "Options for monitoring the solver."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory().initialization()
        info.report(
            (
                f"{self}",
                f"solver = {self.solver}",
                f"initial guess = {self.initial_guess}",
                f"tolerances = {self.tolerances}",
                f"adaptive time stepping = {self.adaptive_ts}",
                f"monitoring = {self.monitoring}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory().todo()
        todo.report(("Implement SolverOptions.__init__(). Pass parameters to C++.",))
        todo.log()
