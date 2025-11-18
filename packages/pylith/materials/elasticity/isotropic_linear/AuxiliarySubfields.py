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

from .... import journal

from ....fields import field, subfields


class AuxiliarySubfields(
    pylith.component,
    implements=field,
    family="pylith.materials.elasticity.isotropic_linear.auxiliary_subfields",
):
    """Auxiliary subfields for isotropic linear bulk rheology."""

    shear_modulus = subfields.subfield(default=subfields.shear_modulus)
    shear_modulus.doc = "Shear modulus."

    bulk_modulus = subfields.subfield(default=subfields.bulk_modulus)
    bulk_modulus.doc = "Bulk modulus."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement IsotropicLinear.__init__(). Pass parameters to C++.",
                f"{self.shear_modulus}",
                f"{self.bulk_modulus}",
            )
        )
        todo.log()
