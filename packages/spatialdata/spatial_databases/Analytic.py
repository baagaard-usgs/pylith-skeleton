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

from ..protocols.spatial_databases import analytic_value
from ..utils import constraints

import spatialdata

from .SpatialDatabaseBase import SpatialDatabaseBase


class Analytic(SpatialDatabaseBase, family="spatialdata.spatial_databsae.analytic"):
    """Analytic values over a domain."""

    values = spatialdata.properties.list(schema=analytic_value)
    values.validators = constraints.notEmptyList()
    values.doc = "Values in spatial database."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = spatialdata.journal.info_factory.initialization(detail=5)
        info.report(
            (
                f"{self}",
                f"values = {self.values}",
            )
        )
        info.log()

        todo = spatialdata.journal.debug_factory.todo()
        todo.report(("Implement Analytic.__init__(). Pass parameters to C++.",))
        todo.log()
