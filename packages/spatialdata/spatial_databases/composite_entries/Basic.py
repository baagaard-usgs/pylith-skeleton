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

from ...protocols import spatial_database
from ...protocols.spatial_databases import composite_entry


class Basic(
    spatialdata.component, implements=composite_entry, family="spatialdata.spatial_databases.composite_entries.basic"
):
    """Basic spatial database in a composite spatial database."""

    values = spatialdata.properties.list(schema=spatialdata.properties.str())
    values.doc = "Names of values to query in spatial database."

    database = spatial_database()
    database.doc = "Spatial database in composite spatial database."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = spatialdata.journal.info_factory.initialization(detail=5)
        info.report(
            (
                f"{self}",
                f"values = {self.values}",
                f"database = {self.database}",
            )
        )
        info.log()

        todo = spatialdata.journal.debug_factory.todo()
        todo.report(("Implement Basic.__init__(). Pass parameters to C++.",))
        todo.log()
