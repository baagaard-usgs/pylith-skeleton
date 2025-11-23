# =================================================================================================
# This code is part of SpatialData, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/spatialdata).
#
# Copyright (c) 2010-2025, University of California, Davis and the SpatialData Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import spatialdata

from ..protocols import coord_sys


class GeographicLocal(spatialdata.component, implements=coord_sys):
    """Geographic coordinate system with local origin and rotation."""

    crs_string = spatialdata.properties.str(default="EPSG:4326")
    crs_string.doc = "String specifying geographic coordinate system (PROJ parameters, EPSG, or WKT)."

    space_dim = spatialdata.properties.int(default=3)
    space_dim.constraints.isMember(2, 3)
    space_dim.doc = "Spatial dimension of coordinate system."

    origin_x = spatialdata.properties.float(default=0.0)
    origin_x.doc = "X coordinate of local origin."

    origin_y = spatialdata.properties.float(default=0.0)
    origin_y.doc = "Y coordinate of local origin."

    y_azimuth = spatialdata.properties.float(default=0.0)
    y_azimuth.doc = "Azimuth of y coordinate axes in degrees (clockwise from north)."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = spatialdata.journal.info_factory.initialization(detail=5)
        info.report(
            (
                f"{self}",
                f"CRS string = {self.crs_string}",
                f"space dim = {self.space_dim}",
                f"origin = ({self.origin_x}, {self.origin_y})",
                f"Y azimuth = {self.y_azimuth}",
            )
        )
        info.log()

        todo = spatialdata.journal.debug_factory.todo()
        todo.report(("Implement GeographicLocal.__init__(). Pass parameters to C++.",))
        todo.log()
