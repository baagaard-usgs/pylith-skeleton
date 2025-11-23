# =================================================================================================
# This code is part of SpatialData, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/spatialdata).
#
# Copyright (c) 2010-2025, University of California, Davis and the SpatialData Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import pyre
from pyre.units.length import meter


import spatialdata

from ..protocols import coord_sys


class Cartesian(spatialdata.component, implements=coord_sys):
    """Cartesian coordinate system."""

    units = spatialdata.properties.dimensional(default=1.0 * meter)
    units.validators = pyre.constraints.isPositive()
    units.doc = "Unit for coordinate axes."

    space_dim = spatialdata.properties.int(default=3)
    space_dim.constraints.isMember(1, 2, 3)
    space_dim.doc = "Spatial dimension of coordinate system."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = spatialdata.journal.info_factory.initialization(detail=5)
        info.report(
            (
                f"{self}",
                f"units = {self.units}",
                f"space dim = {self.space_dim}",
            )
        )
        info.log()

        todo = spatialdata.journal.debug_factory.todo()
        todo.report(("Implement Cartesian.__init__(). Pass parameters to C++.",))
        todo.log()
