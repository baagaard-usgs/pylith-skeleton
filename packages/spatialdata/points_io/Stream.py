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

from ..protocols import points_io


class Stream(spatialdata.component, implements=points_io, family="spatialdata.points_io.stream"):
    """Stream with time history with points."""

    uri = spatialdata.properties.uri(default=None)
    uri.doc = "Data file for Simple spatial database."

    comment_flag = spatialdata.properties.str(default="#")
    comment_flag.doc = "String identifying comments."

    format = spatialdata.properties.str(default="%14.5e")
    format.doc = "C style string specifying number format"

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = spatialdata.journal.info_factory.initialization(detail=5)
        info.report(
            (
                f"{self}",
                f"uri = {self.uri}",
                f"comment_flag = {self.comment_flag}",
                f"format = {self.format}",
            )
        )
        info.log()

        todo = spatialdata.journal.debug_factory.todo()
        todo.report(("Implement Simple.__init__(). Pass parameters to C++.",))
        todo.log()

    def read(self):
        """
        Read points from file.
        """
        import numpy

        points = numpy.loadtxt(self.uri, comments=self.comment_flag)
        return points

    def write(self, points):
        """Write points to file."""
        import numpy

        numpy.savetxt(self.uri, points, fmt=self.format)
        return
