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

from .BoundaryCondition import BoundaryConditionBase


class Dirichlet(BoundaryConditionBase, family="pylith.boundary_conditions.dirichlet"):
    """Dirichlet boundary condition."""

    constrained_dof = pylith.properties.list(schema=int)
    constraind_dof = pyre.constraints.isSubset(choices=(0, 1, 2))
    constrained_dof.doc = "Array of constrained degrees of freedom (0=1st DOF, 1=2nd DOF, etc)."

    use_initial = pylith.properties.bool(default=True)
    use_initial.doc = "Use initial term in time-dependent expression."

    use_rate = pylith.properties.bool(default=False)
    use_rate.doc = "Use rate term in time-dependent expression."

    use_time_history = pylith.properties.bool(default=False)
    use_time_history.doc = "Use time history term in time-dependent expression."

    # time_history = db_time_history()
    # time_history.doc = "Time history with normalized amplitude."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement Dirichlet time_history attribute. Requires spatialdata.",
                "Implement Dirichlet.__init__(). Pass parameters to C++.",
                f"constrained dof={self.constrained_dof}",
                f"use initial={self.use_initial}",
                f"use rate={self.use_rate}",
                f"use time history={self.use_time_history}",
            )
        )
        todo.log()
