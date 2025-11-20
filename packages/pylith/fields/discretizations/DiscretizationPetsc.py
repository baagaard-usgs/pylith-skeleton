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

from ...protocols.fields import discretization


class DiscretizationPetsc(pylith.component, implements=discretization, family="pylith.fields.discretizations.petsc"):
    """PETSc discretization of a subfield."""

    basis_order = pylith.properties.int(default=-1)
    basis_order.doc = "Order of basis functions."

    quadrature_order = pylith.properties.int(default=-1)
    quadrature_order.doc = "Order of numerical quadrature."

    dimension = pylith.properties.int(default=-1)
    dimension.doc = "Topological dimension associated with subfield (=-1 will use dimension of domain)."

    finite_element_space = pylith.properties.str(default="polynomial")
    finite_element_space.validators = pyre.constraints.isMember("polynomial", "point")
    finite_element_space.doc = (
        "Finite-element space (polynomial or point). Point space corresponds to delta functions at quadrature points."
    )

    cell_basis = pylith.properties.str(default="default")
    cell_basis.validators = pyre.constraints.isMember("simplex", "tensor", "default")
    cell_basis.doc = (
        "Type of cell basis functions (simplex, tensor, or default). Default is to use type matching cell type."
    )

    is_basis_continuous = pylith.properties.bool(default=True)
    is_basis_continuous.doc = "Is basis continuous?"

    is_cohesive_only = pylith.properties.bool(default=False)
    is_cohesive_only.doc = "Is subfield limited to cohesive cells?"

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement DiscretizationPetsc.__init__(). Pass parameters to C++.",
                f"basis order={self.basis_order}",
                f"quadrature order={self.quadrature_order}",
                f"dimension={self.dimension}",
                f"finite element space={self.finite_element_space}",
                f"cell basis={self.cell_basis}",
                f"is basis continuous={self.is_basis_continuous}",
                f"is cohesive only={self.is_cohesive_only}",
            )
        )
        todo.log()
