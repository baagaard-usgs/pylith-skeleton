# =================================================================================================
# This code is part of SpatialData, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/spatialdata).
#
# Copyright (c) 2010-2026 All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import spatialdata


@spatialdata.foundry(tip="Points stream")
def stream(**kwds):
    from .Stream import Stream

    __doc__ = Stream.__doc__
    if kwds:
        return Stream(**kwds)
    return Stream


# End of file
