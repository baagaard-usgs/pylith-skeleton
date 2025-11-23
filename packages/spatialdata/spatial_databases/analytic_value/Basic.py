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

from ... import protocols
from ...protocols.spatial_databases import analytic_value


class Basic(
    spatialdata.component, implements=analytic_value, family="spatialdata.spatial_databases.analytic_value.basic"
):
    """Basic value in a uniform spatial database."""

    name = spatialdata.properties.str()
    name.doc = "Name of value in analytic spatial database."

    units = spatialdata.properties.dimensional()
    units.doc = "Units of value in analytic spatial database."

    expression = spatialdata.properties.str()
    expression.doc = "Analytical expression for value in spatial database."

    coord_sys = protocols.coordinate_system()
    coord_sys.doc = "Coordinate system associated with analytical expression."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = spatialdata.journal.info_factory.initialization(detail=5)
        info.report(
            (
                f"{self}",
                f"name = {self.name}",
                f"units = {self.units}",
                f"expression = {self.expression}",
                f"coord_sys = {self.coord_sys}",
            )
        )
        info.log()

        todo = spatialdata.journal.debug_factory.todo()
        todo.report(("Implement Basic.__init__(). Pass parameters to C++.",))
        todo.log()
