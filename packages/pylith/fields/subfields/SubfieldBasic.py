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

from .Subfield import Subfield

from ..discretizations import discretization, petsc


class SubfieldBasic(pyre.component, implements=Subfield, family="pylith.fields.subfields.basic"):
    """Subfield in PETSc field."""

    name = None
    scale = None
    vector_field_type = None
    component_names = None

    alias = pylith.properties.str()
    alias.doc = "User preferred name of Subfield (used in output)."

    discretization = discretization(default=petsc)
    discretization.doc = "Discretization of subfield."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement SubfieldBasic.__init__(). Pass parameters to C++.",
                f"name={self.name}",
                f"alias={self.alias}",
                f"scale={self.scale}",
                f"vector field type={self.vector_field_type}",
                f"components={self.component_names}",
                f"discretization={self.discretization}",
            )
        )
        todo.log()
