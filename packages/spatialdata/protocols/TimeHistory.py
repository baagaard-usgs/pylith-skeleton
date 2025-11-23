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


class TimeHistory(spatialdata.protocol, family="spatialdata.time_histories"):
    """Protocol declarator for time histories."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {BoundaryCondition} implementation"""
        from ..time_histories import points_list

        return points_list
