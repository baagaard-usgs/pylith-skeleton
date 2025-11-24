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

from ..protocols import boundary_condition


class BoundaryConditionBase(pylith.component, implements=boundary_condition):
    """Base class for boundary conditions."""

    field = pylith.properties.str(default="displacement")
    field.doc = "Solution subfield associated with boundary condition."

    label_name = pylith.properties.str(default=None)
    label_name.doc = "Name of label identifying boundary ()name of physical group in Gmsh files."

    label_value = pylith.properties.int(default=1)
    label_value.doc = "Value of label identifying boundary (tag of physical group in Gmsh files)."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization(detail=5)
        info.report(
            (
                f"{self}",
                f"field = {self.field}",
                f"label name = {self.label_name}",
                f"label value = {self.label_value}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement BoundaryConditionBase.__init__(). Pass parameters to C++.",))
        todo.log()
