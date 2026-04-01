# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import pylith


@pylith.foundry(tip="VTK data writer")
def vtk():
    try:
        from .DataWriterVTK import DataWriterVTK
    except ImportError:
        return
    __doc__ = DataWriterVTK.__doc__
    return DataWriterVTK


@pylith.foundry(tip="HDF5 data writer")
def hdf5():
    try:
        from .DataWriterHDF5 import DataWriterHDF5
    except ImportError:
        return
    __doc__ = DataWriterHDF5.__doc__
    return DataWriterHDF5
