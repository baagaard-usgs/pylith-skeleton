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

from pylith.fields import Field, subfields


class Elasticity(
    pylith.component,
    implements=Field,
    family="pylith.materials.auxiliary_subfields.elasticity",
):
    """Auxiliary subfields for elasticity."""

    density = subfields.subfield(default=subfields.density)
    density.doc = "Mass density."

    body_force = subfields.subfield(default=subfields.body_force_optional)
    body_force.doc = "Body force (optional)."

    gravitational_acceleration = subfields.subfield(default=subfields.gravitational_acceleration_optional)
    gravitational_acceleration.doc = "Gravitational acceleration (optional)."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement IsotropicLinear.__init__(). Pass parameters to C++.",
                f"{self.density}",
                f"{self.body_force}",
                f"{self.gravitational_acceleration}",
            )
        )
        todo.log()
