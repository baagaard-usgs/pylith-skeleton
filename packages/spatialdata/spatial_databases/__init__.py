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
def uniform(**kwds):
    from .Uniform import Uniform
    __doc__ = Uniform.__doc__
    if kwds:
        return Uniform(**kwds)
    return Uniform


@spatialdata.foundry(tip="Spatial database defined by analytic functions.")
def analytic(**kwds):
    from .Analytic import Analytic
    __doc__ = Analytic.__doc__
    if kwds:
        return Analytic(**kwds)
    return Analytic


@spatialdata.foundry(tip="Simple spatial database defined by points in space.")
def simple(**kwds):
    from .Simple import Simple
    __doc__ = Simple.__doc__
    if kwds:
        return Simple(**kwds)
    return Simple


@spatialdata.foundry(tip="Spatial database defined by a grid of points.")
def simple_grid(**kwds):
    from .SimpleGrid import SimpleGrid
    __doc__ = SimpleGrid.__doc__
    if kwds:
        return SimpleGrid(**kwds)
    return SimpleGrid


@spatialdata.foundry(tip="Spatial database composed of other spatial databases.")
def composite(**kwds):
    from .Composite import Composite
    __doc__ = Composite.__doc__
    if kwds:
        return Composite(**kwds)
    return Composite


@spatialdata.foundry(tip="Spatial database for a gravitational acceleration.")
def gravity_field(**kwds):
    from .GravityField import GravityField
    __doc__ = GravityField.__doc__
    if kwds:
        return GravityField(**kwds)
    return GravityField
