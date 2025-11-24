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

from .BoundaryConditionBase import BoundaryConditionBase


class Dirichlet(BoundaryConditionBase, family="pylith.boundary_conditions.dirichlet"):
    """Dirichlet boundary condition."""

    constrained_dof = pylith.properties.strings()
    constraind_dof = pyre.constraints.isSubset(choices=("x", "y", "z"))
    constrained_dof.doc = "Array of constrained degrees of freedom."

    # :TODO: Add auxiliary subfields

    # time_history = db_time_history()
    # time_history.doc = "Time history with normalized amplitude."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization(detail=5)
        info.detail = 5
        info.report(
            (
                f"{self}",
                f"constrained dof = {self.constrained_dof}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(
            (
                "Implement Dirichlet.__init__(). Pass parameters to C++.",
                "Add auxiliary subfields.",
                "Implement Dirichlet time_history attribute. Requires spatialdata.",
            )
        )
        todo.log()

    def pyre_configured(self):
        """Called after component is configured."""
        yield from super().pyre_configured()

        if len(self.constrained_dof) == 0:
            msg = (
                "Missing constrained degrees of freedom.",
                "Specify 'constrained_dof' or remove this Dirichlet boundary condition.",
            )
            ex = pylith.exceptions.ConfigurationError(component=self, msg=msg)
            yield ex
