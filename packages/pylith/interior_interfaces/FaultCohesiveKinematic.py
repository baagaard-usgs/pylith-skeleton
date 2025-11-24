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


from .FaultCohesive import FaultCohesive
from ..protocols.interior_interfaces import source_time_fn

from .source_time_fns import step


class FaultCohesiveKinematic(FaultCohesive, family="pylith.interior_interfaces.fault_cohesive_kinematic"):
    """Fault with kinematic earthquake sources."""

    eq_ruptures = pylith.properties.list(schema=source_time_fn(default=step))
    eq_ruptures.doc = "Earthquake ruptures with kinematic source parameters (prescribed slip)."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"earthquake ruptures = {self.eq_ruptures}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement FaultCohesiveKinematic.__init__(). Pass parameters to C++.",))
        todo.log()
