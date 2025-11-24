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


class SubfieldsNoFault(
    pylith.component,
    implements=solution_subfields,
    family="pylith.governing_eqns.elasticity.solution_subfields.nofault",
):
    """Solution subfields for elasticity equation without a fault."""

    displacement = subfield(default=basic)
    displacement.doc = "Displacement subfield."

    velocity = subfield(default=basic)
    velocity.doc = "Velocity subfield."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"displacement = {self.displacement}",
                f"velocity = {self.velocity}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement SubfieldsNoFault.__init__(). Pass parameters to C++.",))
        todo.log()
