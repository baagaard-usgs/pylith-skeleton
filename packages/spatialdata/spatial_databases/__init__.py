# =================================================================================================
# This code is part of SpatialData, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/spatialdata).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import spatialdata


@spatialdata.foundry(tip="Spatial database with uniform values.")
def uniform():
    try:
        from .Uniform import Uniform
    except ImportError:
        return
    __doc__ = Uniform.__doc__
    return Uniform


@spatialdata.foundry(tip="Spatial database defined by analytic functions.")
def analytic():
    try:
        from .Analytic import Analytic
    except ImportError:
        return
    __doc__ = Analytic.__doc__
    return Analytic


@spatialdata.foundry(tip="Simple spatial database defined by points in space.")
def simple():
    try:
        from .Simple import Simple
    except ImportError:
        return
    __doc__ = Simple.__doc__
    return Simple


@spatialdata.foundry(tip="Spatial database defined by a grid of points.")
def simple_grid():
    try:
        from .SimpleGrid import SimpleGrid
    except ImportError:
        return
    __doc__ = SimpleGrid.__doc__
    return SimpleGrid


@spatialdata.foundry(tip="Spatial database composed of other spatial databases.")
def composite():
    try:
        from .Composite import Composite
    except ImportError:
        return
    __doc__ = Composite.__doc__
    return Composite


@spatialdata.foundry(tip="Spatial database for a gravitational acceleration.")
def gravity_field():
    try:
        from .GravityField import GravityField
    except ImportError:
        return
    __doc__ = GravityField.__doc__
    return GravityField
