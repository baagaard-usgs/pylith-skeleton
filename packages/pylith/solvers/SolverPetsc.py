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

from ..protocols import solver, petsc
from ..petsc.options import solver_options


class SolverPetsc(pylith.component, implements=solver, family="pylith.solvers.petsc"):
    """PETSc solver."""

    formulation = pylith.properties.str(default="implicit")
    formulation.validators = pyre.constraints.isMember("implicit", "explicit", "implicit_explicit")
    formulation.doc = "Formulation for solver."

    petsc_options = petsc.options_manager(default=solver_options)
    petsc_options.doc = "Groups of solver related PETSc options."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"formulation = {self.formulation}",
                f"PETSc options = {self.petsc_options}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement SolverPetsc.__init__(). Pass parameters to C++.",))
        todo.log()

    def pyre_configured(self):
        """Called after component is configured."""
        yield from super().pyre_configured()

        from ..petsc.options.groups import group_list

        if hasattr(self.petsc_options, "solver") and isinstance(self.petsc_options.solver, group_list):
            options = self.petsc_options.solver
            if options.enabled and len(options.options) == 0:
                msg = (
                    "PETSc solver options group 'solver' is enabled but has no options.",
                    "Specify solver options or disable the group if you specify your PETSc options directly.",
                )

                ex = pylith.exceptions.ConfigurationError(component=self, msg=msg)
                yield ex
