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

from ..utils import constraints

from ..protocols import interior_interface


class FaultCohesive(pylith.component, implements=interior_interface):
    """Abstract base class for faults implemented with cohesive cells."""

    label_name = pylith.properties.str(default=None)
    label_name.doc = "Name of label identifying boundary ()name of physical group in Gmsh files."

    label_value = pylith.properties.int(default=1)
    label_value.doc = "Value of label identifying boundary (tag of physical group in Gmsh files)."

    edge_label_name = pylith.properties.str()
    edge_label_name.doc = "Name of label identifier for buried fault edges."

    edge_label_value = pylith.properties.int(default=1)
    edge_label_value.doc = "Value of label identifier for buried fault edges."

    ref_dir_1 = pylith.properties.list(schema=pylith.properties.float(), default=[0.0, 0.0, 1.0])
    ref_dir_1.validators = constraints.unitVector()
    ref_dir_1.doc = "First choice for reference direction to discriminate among tangential directions in 3-D."

    ref_dir_2 = pylith.properties.list(schema=pylith.properties.float(), default=[0.0, 1.0, 0.0])
    ref_dir_2.validators = constraints.unitVector()
    ref_dir_2.doc = "Second choice for reference direction to discriminate among tangential directions in 3-D."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement BoundaryCondition.__init__(). Pass parameters to C++.",
                f"label name={self.label_name}",
                f"label value={self.label_value}",
                f"edge label name={self.edge_label_name}",
                f"edge label value={self.edge_label_value}",
                f"reference direction 1={self.ref_dir_1}",
                f"reference direction 2={self.ref_dir_2}",
            )
        )
        todo.log()
