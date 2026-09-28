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
def cartesian(**kwds):
    from .Cartesian import Cartesian
    __doc__ = Cartesian.__doc__
    if kwds:
        return Cartesian(**kwds)
    return Cartesian


@spatialdata.foundry(tip="Geographic coordinate system")
def geographic(**kwds):
    from .Geographic import Geographic
    __doc__ = Geographic.__doc__
    if kwds:
        return Geographic(**kwds)
    return Geographic


@spatialdata.foundry(tip="Geographic coordinate system with local origin")
def geographic_local(**kwds):
    from .GeographicLocal import GeographicLocal
    __doc__ = GeographicLocal.__doc__
    if kwds:
        return GeographicLocal(**kwds)
    return GeographicLocal
