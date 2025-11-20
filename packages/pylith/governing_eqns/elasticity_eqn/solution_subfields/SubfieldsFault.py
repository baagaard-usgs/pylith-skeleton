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


from ....protocols.fields import subfield
from ....protocols.governing_eqns.elasticity import solution_subfields

from ....fields.subfields import basic


class SubfieldsFault(
    pylith.component, implements=solution_subfields, family="pylith.governing_eqns.elasticity.solution_subfields.fault"
):
    """Solution subfields for elasticity equation with a fault."""

    displacement = subfield(default=basic)
    displacement.doc = "Displacement subfield."

    velocity = subfield(default=basic)
    velocity.doc = "Velocity subfield."

    lagrange_multiplier_fault = subfield(default=basic)
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
