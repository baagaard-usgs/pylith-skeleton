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


from .FaultCohesive import FaultCohesive
from .source_time_fns import source_time_fn


class FaultCohesiveKinematic(FaultCohesive, family="pylith.interior_interfaces.fault_cohesive_kinematic"):
    """Fault with kinematic earthquake sources."""

    eq_ruptures = pylith.properties.list(schema=source_time_fn())
    eq_ruptures.doc = "Earthquake ruptures with kinematic source parameters (prescribed slip)."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.warning(":TODO:")
        todo.report(
            (
                "Implement FaultCohesiveKinematic.__init__(). Pass parameters to C++.",
                f"earthquake ruptures={self.eq_ruptures}",
            )
        )
        todo.log()
