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

from pylith import journal
from pylith import fields


class BulkRheology(pylith.protocol, family="pylith.materials.elasticity_rheologies"):
    """Protocol declarator for BulkRheology."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {BulkRheology} implementation"""
        from .IsotropicLinear import IsotropicLinear

        return IsotropicLinear


class BulkRheologyBase(pylith.component, implements=BulkRheology):

    auxiliary_subfields = fields.optional()
    auxiliary_subfields.doc = "Rheologic-specific material parameters."

    derived_subfields = fields.optional()
    derived_subfields.doc = "Rheologic-specific output subfields derived from solution and bulk rheology."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.warning(":TODO:")
        todo.report(
            (
                "Implement BulkRheologyBase.__init__(). Pass parameters to C++.",
                f"auxiliary subfields={self.auxiliary_subfields}",
                f"derived subfields={self.derived_subfields}",
            )
        )
        todo.log()
