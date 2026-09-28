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


@pylith.foundry(tip="Output observer")
def output_observer(**kwds):
    from .OutputObserver import OutputObserver
    __doc__ = OutputObserver.__doc__
    if kwds:
        return OutputObserver(**kwds)
    return OutputObserver


@pylith.foundry(tip="Output solution domain")
def solution_domain(**kwds):
    from .OutputSolnDomain import OutputSolnDomain
    __doc__ = OutputSolnDomain.__doc__
    if kwds:
        return OutputSolnDomain(**kwds)
    return OutputSolnDomain


@pylith.foundry(tip="Output solution boundary")
def solution_boundary(**kwds):
    from .OutputSolnBoundary import OutputSolnBoundary
    __doc__ = OutputSolnBoundary.__doc__
    if kwds:
        return OutputSolnBoundary(**kwds)
    return OutputSolnBoundary


@pylith.foundry(tip="Output solution points")
def solution_points(**kwds):
    from .OutputSolnPoints import OutputSolnPoints
    __doc__ = OutputSolnPoints.__doc__
    if kwds:
        return OutputSolnPoints(**kwds)
    return OutputSolnPoints


@pylith.foundry(tip="Output physics")
def output_physics(**kwds):
    from .OutputPhysics import OutputPhysics
    __doc__ = OutputPhysics.__doc__
    if kwds:
        return OutputPhysics(**kwds)
    return OutputPhysics
