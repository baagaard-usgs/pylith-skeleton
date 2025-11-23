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


class SpatialDatabase(spatialdata.protocol, family="spatialdata.spatial_databases"):
    """Protocol declarator for spatial databases."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {BoundaryCondition} implementation"""
        from ..spatial_databases import uniform

        return uniform
