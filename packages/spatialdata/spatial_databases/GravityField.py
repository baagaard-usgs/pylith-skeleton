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
from pyre.units.time import second

import spatialdata

from .SpatialDatabaseBase import SpatialDatabaseBase
from ..utils import constraints


class GravityField(SpatialDatabaseBase, family="spatialdata.spatial_databases.gravity_field"):
    """Spatial database for a gravity field."""

    gravity_dir = spatialdata.properties.list(schema=spatialdata.properties.float(), default=[0.0, 0.0, -1.0])
    gravity_dir.validators = constraints.unitVector()
    gravity_dir.doc = "Direction of gravitational body force (only used with Cartesian coordinate system)."

    acceleration = spatialdata.properties.dimensional(default=9.80665 * meter / second)
    acceleration.doc = "Gravitational acceleration."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = spatialdata.journal.info_factory.initialization(detail=5)
        info.report(
            (
                f"{self}",
                f"gravity_dir = {self.gravity_dir}",
                f"acceleration = {self.acceleration}",
            )
        )
        info.log()

        todo = spatialdata.journal.debug_factory.todo()
        todo.report(("Implement GravityField.__init__(). Pass parameters to C++.",))
        todo.log()
