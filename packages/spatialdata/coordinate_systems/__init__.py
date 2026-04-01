# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import spatialdata


@spatialdata.foundry(tip="Cartesian coordinate system")
def cartesian():
    try:
        from .Cartesian import Cartesian
    except ImportError:
        return
    __doc__ = Cartesian.__doc__
    return Cartesian


@spatialdata.foundry(tip="Geographic coordinate system")
def geographic():
    try:
        from .Geographic import Geographic
    except ImportError:
        return
    __doc__ = Geographic.__doc__
    return Geographic


@spatialdata.foundry(tip="Geographic coordinate system with local origin")
def geographic_local():
    try:
        from .GeographicLocal import GeographicLocal
    except ImportError:
        return
    __doc__ = GeographicLocal.__doc__
    return GeographicLocal
