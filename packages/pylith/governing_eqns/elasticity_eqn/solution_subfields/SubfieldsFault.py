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


from ....fields import subfields

from .SolutionSubfields import SolutionSubfields


class SubfieldsFault(
    pylith.component, implements=SolutionSubfields, family="pylith.governing_eqns.elasticity.solution_subfields.fault"
):
    """Solution subfields for elasticity equation with a fault."""

    displacement = subfields.subfield(default=subfields.basic)
    displacement.doc = "Displacement subfield."

    velocity = subfields.subfield(default=subfields.basic)
    velocity.doc = "Velocity subfield."

    lagrange_multiplier_fault = subfields.subfield(default=subfields.basic)
    lagrange_multiplier_fault.doc = "Fault Lagrange multiplier subfield."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement SubfieldsFault.__init__(). Pass parameters to C++.",
                f"displacement={self.displacement}",
                f"velocity={self.velocity}",
                f"Lagrange multiplier fault={self.lagrange_multiplier_fault}",
            )
        )
        todo.log()
