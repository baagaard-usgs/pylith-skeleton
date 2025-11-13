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

from .Container import Container
from .. import subfields


class ElasticitySubfields(
    pylith.component, implements=Container, family="pylith.fields.containers.elasticity_subfields"
):
    """Elasticity subfields."""

    density = subfields.density()
    density.doc = "Density subfield."

    body_force = subfields.body_force_optional()
    body_force.doc = "Body force (optional)."

    gravitational_acceleration = subfields.gravity_optional()
    gravitational_acceleration.doc = "Gravitational acceleration (optional)."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement Elasticity.__init__(). Pass parameters to C++.",
                f"density={self.density}",
                f"body force={self.body_force}",
                f"gravitational acceleration={self.gravitational_acceleration}",
            )
        )
        todo.log()
