# =================================================================================================
# This code is part of SpatialData, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/spatialdata).
#
# Copyright (c) 2010-2026 All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import spatialdata


class AnalyticValue(spatialdata.protocol, family="spatialdata.spatial_databases.analytic_values"):
    """Protocol declarator for values in an analytic spatial database."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {AnalyticValue} implementation"""
        from ...spatial_databases.uniform_values import basic

        return basic


# End of file
