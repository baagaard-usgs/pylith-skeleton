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

from ..protocols import time_history


class Points(spatialdata.component, implements=time_history, family="spatialdata.time_histories.points"):
    """Time history with points in time."""

    description = spatialdata.properties.str()
    description.doc = "Description of time history."

    filename = spatialdata.properties.uri()
    filename.doc = "Data file for time history."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = spatialdata.journal.info_factory.initialization(detail=5)
        info.report(
            (
                f"{self}",
                f"description = {self.description}",
                f"filename = {self.filename}",
            )
        )
        info.log()

        todo = spatialdata.journal.debug_factory.todo()
        todo.report(("Implement Points.__init__(). Pass parameters to C++.",))
        todo.log()
