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
def brune():
    try:
        from .Brune import Brune
    except ImportError:
        return
    __doc__ = Brune.__doc__
    return Brune


@pylith.foundry(tip="Constant rate source time function")
def constant_rate():
    try:
        from .ConstantRate import ConstantRate
    except ImportError:
        return
    __doc__ = ConstantRate.__doc__
    return ConstantRate


@pylith.foundry(tip="Liu cosine source time function")
def liu_cosine():
    try:
        from .LuiCosine import LiuCosine
    except ImportError:
        return
    __doc__ = LiuCosine.__doc__
    return LiuCosine


@pylith.foundry(tip="Ramp source time function")
def ramp():
    try:
        from .Ramp import Ramp
    except ImportError:
        return
    __doc__ = Ramp.__doc__
    return Ramp


@pylith.foundry(tip="Step source time function")
def step():
    try:
        from .Step import Step
    except ImportError:
        return
    __doc__ = Step.__doc__
    return Step


@pylith.foundry(tip="Time history source time function")
def time_history():
    try:
        from .TimeHistory import TimeHistory
    except ImportError:
        return
    __doc__ = TimeHistory.__doc__
    return TimeHistory
