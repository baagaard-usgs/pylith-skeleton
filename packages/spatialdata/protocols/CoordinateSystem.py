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


class CoordinateSystem(spatialdata.protocol, family="spatialdata.coordinate_systems"):
    """Protocol declarator for coordinate systems."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {CoordinateSystem} implementation"""
        from ..coordinate_systems import cartesian

        return cartesian
