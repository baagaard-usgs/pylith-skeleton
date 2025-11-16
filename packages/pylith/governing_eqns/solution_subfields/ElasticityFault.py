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

from pylith.fields import subfields

from .Solution import Solution


class ElasticityFault(pylith.component, implements=Solution, family="pylith.governing_eqns.solutions.elasticity_fault"):
    """Solution subfields for elasticity equation with a fault."""

    displacement = subfields.subfield(default=subfields.displacement)
    displacement.doc = "Displacment subfield."

    velocity = subfields.subfield(default=subfields.velocity)
    velocity.doc = "Velocity subfield."

    lagrange_multiplier_fault = subfields.subfield(default=subfields.lagrange_multiplier_fault)
    lagrange_multiplier_fault.doc = "Fault Lagrange multiplier subfield."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement ElasticityFault.__init__(). Pass parameters to C++.",
                f"displacement={self.displacement}",
                f"velocity={self.velocity}",
                f"Lagrange multiplier fault={self.lagrange_multiplier_fault}",
            )
        )
        todo.log()
