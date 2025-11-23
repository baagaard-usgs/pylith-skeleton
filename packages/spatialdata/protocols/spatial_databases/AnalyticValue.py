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


class AnalyticValue(spatialdata.protocol, family="spatialdata.spatial_databases.analytic_value"):
    """Protocol declarator for values in a analytic spatial database."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {AnalyticValue} implementation"""
        from ...spatial_databases.uniform_value import basic

        return basic
