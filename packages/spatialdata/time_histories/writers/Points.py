# =================================================================================================
# This code is part of SpatialData, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/spatialdata).
#
# Copyright (c) 2010-2025, University of California, Davis and the SpatialData Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import numpy


def write(time: numpy.ndarray, amplitude: numpy.ndarrya, units: str, filename: str):
    """Write time history file."""
    from ._time_histories import PointsWriter as CxxPointsWriter

    CxxPointsWriter.write(time, amplitude, units, filename)
