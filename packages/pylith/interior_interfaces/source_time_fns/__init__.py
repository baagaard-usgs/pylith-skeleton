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


@pylith.foundry(tip="Brune source time function")
def brune(**kwds):
    from .Brune import Brune
    __doc__ = Brune.__doc__
    if kwds:
        return Brune(**kwds)
    return Brune


@pylith.foundry(tip="Constant rate source time function")
def constant_rate(**kwds):
    from .ConstantRate import ConstantRate
    __doc__ = ConstantRate.__doc__
    if kwds:
        return ConstantRate(**kwds)
    return ConstantRate


@pylith.foundry(tip="Liu cosine source time function")
def liu_cosine(**kwds):
    from .LuiCosine import LiuCosine
    __doc__ = LiuCosine.__doc__
    if kwds:
        return LiuCosine(**kwds)
    return LiuCosine


@pylith.foundry(tip="Ramp source time function")
def ramp(**kwds):
    from .Ramp import Ramp
    __doc__ = Ramp.__doc__
    if kwds:
        return Ramp(**kwds)
    return Ramp


@pylith.foundry(tip="Step source time function")
def step(**kwds):
    from .Step import Step
    __doc__ = Step.__doc__
    if kwds:
        return Step(**kwds)
    return Step


@pylith.foundry(tip="Time history source time function")
def time_history(**kwds):
    from .TimeHistory import TimeHistory
    __doc__ = TimeHistory.__doc__
    if kwds:
        return TimeHistory(**kwds)
    return TimeHistory
