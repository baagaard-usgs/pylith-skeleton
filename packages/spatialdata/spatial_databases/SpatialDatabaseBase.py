# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import spatialdata

from ..protocols import spatial_database


class SpatialDatabaseBase(spatialdata.component, implements=spatial_database):
    """Base class for spatial databases."""

    description = spatialdata.properties.str()
    description.doc = "Description of spatial database."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = spatialdata.journal.info_factory().initialization(detail=5)
        info.report(
            (
                f"{self}",
                f"description = {self.description}",
            )
        )
        info.log()

        todo = spatialdata.journal.debug_factory().todo()
        todo.report(("Implement SpatialDatabaseBase.__init__(). Pass parameters to C++.",))
        todo.log()
