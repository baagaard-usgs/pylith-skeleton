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
import spatialdata

from .SpatialDatabaseBase import SpatialDatabaseBase


class SimpleGrid(SpatialDatabaseBase, family="spatialdata.spatial_databases.simple_grid"):
    """SimpleGrid spatial database with points on a logical grid."""

    uri = spatialdata.properties.uri(default=None)
    uri.doc = "Data file for SimpleGrid spatial database."

    query_type = spatialdata.properties.str(default="linear")
    query_type.validators = pyre.constraints.isMember("linear", "nearest")
    query_type.doc = "Type of interpolation to use."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = spatialdata.journal.info_factory().initialization(detail=5)
        info.report(
            (
                f"{self}",
                f"uri = {self.uri}",
                f"query_type = {self.query_type}",
            )
        )
        info.log()

        todo = spatialdata.journal.debug_factory().todo()
        todo.report(("Implement SimpleGrid.__init__(). Pass parameters to C++.",))
        todo.log()
