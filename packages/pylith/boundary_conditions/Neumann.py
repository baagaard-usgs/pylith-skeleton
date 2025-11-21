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
from ..utils import constraints

from .BoundaryConditionBase import BoundaryConditionBase


class Neumann(
    BoundaryConditionBase,
    family="pylith.boundary_conditions.neumann",
):
    """Neumann boundary condition.

        This boundary condition applies a Neumann boundary condition for a single solution subfield on a boundary.
        To apply Neumann boundary conditions for multiple solution subfields on a boundary, use multiple Neumann boundary conditions.

        :::{important}
        The components are specified in the local normal-tangential coordinate system for the boundary. Ambiguities in specifying the shear (tangential) tracti
    ons in 3D problems are resolved using the `ref_dir_1` and `ref_dir_2` properties.
        The first tangential direction is $\\vec{z} \\times \\vec{r}_1$ unless these are colinear, then $\\vec{r}_2$ (`ref_dir_2`) is used.
        The second tangential direction is $\\vec{n} \\times \\vec{t}_1$.
        :::

        :::{seealso}
        See [`AuxSubfieldsTimeDependent` Component](AuxSubfieldsTimeDependent.md) for the functional form of the time depenence.
        :::
    """

    scale_name = pylith.properties.str(default="stress")
    scale_name.validators = pyre.constraints.isMember("displacement", "stress")
    scale_name.doc = "Type of scale for nondimensionalizing Neumann boundary condition ('stress' for elasticity)."

    # time_history = db_time_history()
    # time_history.doc = "Time history with normalized amplitude."

    ref_dir_1 = pylith.properties.list(schema=pylith.properties.float(), default=[0.0, 0.0, 1.0])
    ref_dir_1.validators = constraints.unitVector()
    ref_dir_1.doc = "First choice for reference direction to discriminate among tangential directions in 3D."

    ref_dir_2 = pylith.properties.list(schema=pylith.properties.float(), default=[0.0, 1.0, 0.0])
    ref_dir_2.validators = constraints.unitVector()
    ref_dir_2.doc = "Second choice for reference direction to discriminate among tangential directions in 3D."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization(detail=5)
        info.detail = 5
        info.report(
            (
                f"{self}",
                f"scale name = {self.scale_name}",
                f"ref dir 1 = {self.ref_dir_1}",
                f"ref dir 2 = {self.ref_dir_2}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(
            (
                "Implement Neumann time_history attribute. Requires spatialdata.",
                "Implement Neumann.__init__(). Pass parameters to C++.",
            )
        )
        todo.log()
