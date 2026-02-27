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

from ..protocols.spatial_databases import composite_entry
from ..utils import constraints

from .SpatialDatabaseBase import SpatialDatabaseBase


class Composite(SpatialDatabaseBase, family="spatialdata.spatial_databases.composite"):
    """Composite spatial database with points in space."""

    databases = spatialdata.properties.list(schema=composite_entry())
    databases.validators = constraints.notEmptyList()
    databases.doc = "Spatial databases in composite spatial database."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = spatialdata.journal.info_factory.initialization(detail=5)
        info.report(
            (
                f"{self}",
                f"databases = {self.databases}",
            )
        )
        info.log()

        todo = spatialdata.journal.debug_factory.todo()
        todo.report(("Implement Composite.__init__(). Pass parameters to C++.",))
        todo.log()
