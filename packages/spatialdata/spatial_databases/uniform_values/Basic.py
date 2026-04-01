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

from ...protocols.spatial_databases import uniform_value


class Basic(
    spatialdata.component, implements=uniform_value, family="spatialdata.spatial_databases.uniform_values.basic"
):
    """Basic value in a uniform spatial database."""

    name = spatialdata.properties.str()
    name.doc = "Name of value in uniform spatial database."

    value = spatialdata.properties.dimensional()
    value.doc = "Value in uniform spatial database."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = spatialdata.journal.info_factory().initialization(detail=5)
        info.report(
            (
                f"{self}",
                f"name = {self.name}",
                f"value = {self.value}",
            )
        )
        info.log()

        todo = spatialdata.journal.debug_factory().todo()
        todo.report(("Implement Basic.__init__(). Pass parameters to C++.",))
        todo.log()
