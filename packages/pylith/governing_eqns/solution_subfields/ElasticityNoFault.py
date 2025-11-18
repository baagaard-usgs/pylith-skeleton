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


from ...fields import subfields

from .Solution import Solution


class ElasticityNoFault(
    pylith.component, implements=Solution, family="pylith.governing_eqns.solutions.elasticity_nofault"
):
    """Solution subfields for elasticity equation without a fault."""

    displacement = subfields.subfield(default=subfields.displacement)
    displacement.doc = "Displacment subfield."

    velocity = subfields.subfield(default=subfields.velocity)
    velocity.doc = "Velocity subfield."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement ElasticityFault.__init__(). Pass parameters to C++.",
                f"displacement={self.displacement}",
                f"velocity={self.velocity}",
            )
        )
        todo.log()
