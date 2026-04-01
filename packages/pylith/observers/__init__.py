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
def output_observer():
    try:
        from .OutputObserver import OutputObserver
    except ImportError:
        return
    __doc__ = OutputObserver.__doc__
    return OutputObserver


@pylith.foundry(tip="Output solution domain")
def solution_domain():
    try:
        from .OutputSolnDomain import OutputSolnDomain
    except ImportError:
        return
    __doc__ = OutputSolnDomain.__doc__
    return OutputSolnDomain


@pylith.foundry(tip="Output solution boundary")
def solution_boundary():
    try:
        from .OutputSolnBoundary import OutputSolnBoundary
    except ImportError:
        return
    __doc__ = OutputSolnBoundary.__doc__
    return OutputSolnBoundary


@pylith.foundry(tip="Output solution points")
def solution_points():
    try:
        from .OutputSolnPoints import OutputSolnPoints
    except ImportError:
        return
    __doc__ = OutputSolnPoints.__doc__
    return OutputSolnPoints


@pylith.foundry(tip="Output physics")
def output_physics():
    try:
        from .OutputPhysics import OutputPhysics
    except ImportError:
        return
    __doc__ = OutputPhysics.__doc__
    return OutputPhysics
