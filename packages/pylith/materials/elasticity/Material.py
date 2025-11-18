# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
from pylith import journal

from ... import fields
from ..MaterialBase import MaterialBase
from .BulkRheology import BulkRheology as bulk_rheology
from . import isotropic_linear


class Material(MaterialBase, family="pylith.materials.elasticity"):
    """Elasticity material behavior."""

    rheology = bulk_rheology(default=isotropic_linear.bulk_rheology)
    rheology.doc = "Bulk rheology for elastic material."

    auxiliary_subfields = fields.field(default=isotropic_linear.auxiliary_subfields)
    auxiliary_subfields.doc = "Rheology-specific material parameters."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                f"Implement {__class__}.__init__(). Pass parameters to C++.",
                f"rheology={self.rheology}",
                f"auxiliary subfields={self.auxiliary_subfields}",
            )
        )
        todo.log()
