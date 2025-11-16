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

from .BulkRheology import BulkRheology
from ... import fields
from . import auxiliary_subfields
from . import derived_subfields


class IsotropicLinear(
    pylith.component, implements=BulkRheology, family="pylith.materials.elasticity_rheologies.isotropic_linear"
):
    """Isostropic linear bulk rheology for elasticity."""

    auxiliary_subfields = fields.field(default=auxiliary_subfields.isotropic_linear)
    auxiliary_subfields.doc = "Rheologic-specific material parameters."

    derived_subfields = fields.field(default=derived_subfields.isotropic_linear)
    derived_subfields.doc = "Rheologic-specific output subfields derived from solution and bulk rheology."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.warning(":TODO:")
        todo.report(
            (
                f"{self.pyre_name}",
                "Implement IsotropicLinear.__init__(). Pass parameters to C++.",
                f"{self.auxiliary_subfields}",
                f"{self.derived_subfields}",
            )
        )
        todo.log()
