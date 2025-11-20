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

from ..petsc import options

from .Solver import Solver


class SolverPetsc(pylith.component, implements=Solver, family="pylith.solvers.petsc"):
    """PETSc solver."""

    formulation = pylith.properties.str(default="implicit")
    formulation.validators = pyre.constraints.isMember("implicit", "explicit", "implicit_explicit")
    formulation.doc = "Formulation for solver."

    petsc_options = options.options(default=options.solver_options)
    petsc_options.doc = "Groups of solver related PETSc options."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement SolverPetsc.__init__(). Pass parameters to C++.",
                f"formulation={self.formulation}",
                f"PETSc options={self.petsc_options}",
            )
        )
        todo.log()

    def pyre_initialized(self):
        """Called after component is initialized."""
        from ..petsc.options.groups import group_list

        yield super().pyre_initialized()

        if hasattr(self.petsc_options, "solver") and isinstance(self.petsc_options.solver, group_list):
            solver_options = self.petsc_options.solver
            if solver_options.enabled and len(solver_options.options) == 0:
                yield "PETSc solver options group 'solver' is enabled but has no options. Specify solver options or disable the group."
        import pdb

        pdb.set_trace()
