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

from ..fields import field, subfields

from .Material import MaterialBase
from .elasticity_rheologies import bulk_rheology, isotropic_linear


class AuxiliarySubfields(
    pylith.component,
    implements=field,
    family="pylith.materials.elasticity.auxiliary_subfields",
):
    """Auxiliary subfields for elasticity."""

    density = subfields.subfield(default=subfields.density)
    density.doc = "Mass density."

    # body_force = subfields.subfield(default=subfields.body_force_optional)
    # body_force.doc = "Body force (optional)."

    # gravitational_acceleration = subfields.subfield(default=subfields.gravitational_acceleration_optional)
    # gravitational_acceleration.doc = "Gravitational acceleration (optional)."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                f"Implement {__class__}.__init__(). Pass parameters to C++.",
                f"{self.density}",
                # f"{self.body_force}",
                # f"{self.gravitational_acceleration}",
            )
        )
        todo.log()


class Elasticity(MaterialBase, family="pylith.materials.elasticity"):
    """Elasticity material behavior."""

    rheology = bulk_rheology(default=isotropic_linear)
    rheology.doc = "Bulk rheology for elastic material."

    auxiliary_subfields = field(default=AuxiliarySubfields)
    auxiliary_subfields.doc = "Rheology-specific material parameters."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                f"Implement {__class__}.__init__(). Pass parameters to C++.",
                f"rheology={self.rheology}",
                f"auxiliary subfields={self.auxiliary_subfields}",
            )
        )
        todo.log()
