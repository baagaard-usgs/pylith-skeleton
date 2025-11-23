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


class Geographic(spatialdata.component, implements=coord_sys):
    """Geographic coordinate system."""

    crs_string = spatialdata.properties.str(default="EPSG:4326")
    crs_string.doc = "String specifying geographic coordinate system (PROJ parameters, EPSG, or WKT)."

    space_dim = spatialdata.properties.int(default=3)
    space_dim.constraints.isMember(2, 3)
    space_dim.doc = "Spatial dimension of coordinate system."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = spatialdata.journal.info_factory.initialization(detail=5)
        info.report(
            (
                f"{self}",
                f"CRS string = {self.crs_string}",
                f"space dim = {self.space_dim}",
            )
        )
        info.log()

        todo = spatialdata.journal.debug_factory.todo()
        todo.report(("Implement Geographic.__init__(). Pass parameters to C++.",))
        todo.log()
