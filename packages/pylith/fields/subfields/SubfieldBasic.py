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

from ...protocols import fields

from ..discretizations import petsc


class SubfieldBasic(pylith.component, implements=fields.subfield, family="pylith.fields.subfields.basic"):
    """Subfield in PETSc field."""

    alias = pylith.properties.str()
    alias.doc = "User-preferred name of Subfield (used in output)."

    discretization = fields.discretization(default=petsc)
    discretization.doc = "Discretization of subfield."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement SubfieldBasic.__init__(). Pass parameters to C++.",
                f"alias={self.alias}",
                f"discretization={self.discretization}",
            )
        )
        todo.log()
