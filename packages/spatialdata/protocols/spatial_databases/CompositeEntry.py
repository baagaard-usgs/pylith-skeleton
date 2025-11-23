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


class CompositeEntry(spatialdata.protocol, family="spatialdata.spatial_databases.composite_entry"):
    """Protocol declarator for spatial databases in a composite spatial database."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {CompositeEntry} implementation"""
        from ...spatial_databases.composite_entry import basic

        return basic
