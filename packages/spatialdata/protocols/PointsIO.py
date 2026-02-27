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


class PointIO(spatialdata.protocol, family="spatialdata.point_io"):
    """Protocol declarator for points I/O."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {BoundaryCondition} implementation"""
        from ..point_io import points_stream

        return points_stream
