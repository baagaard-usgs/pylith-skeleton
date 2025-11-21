# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import pyre

from pyre.units.length import meter

import pylith


from .FaultCohesive import FaultCohesive


class FaultCohesiveImpulses(FaultCohesive, family="pylith.interior_interfaces.fault_cohesive_kinematic"):
    """Fault with kinematic earthquake sources."""

    # db_auxiliary_field = spatialdb_auxiliary_field()
    # db_auxiliary_field.doc = ""

    threshold = pylith.properties.dimensional(default=1.0e-3 * meter)
    threshold.validators = pyre.constraints.isGreaterEqual(value=0.0 * meter)
    threshold.doc = "Threshold for non-zero amplitude."

    impulse_dof = pylith.properties.list(schema=pylith.properties.int())
    impulse_dof.validators = pyre.constraints.isSubset(choices=(0, 1, 2))
    impulse_dof.doc = "Indices of impulse components; 0=fault opening, 1=left lateral, 2=reverse (3D only)."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"threshold = {self.threshold}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement FaultCohesiveImpulses.__init__(). Pass parameters to C++.",))
        todo.log()
