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


@pylith.foundry(tip="Output trigger step")
def step(**kwds):
    from .OutputTriggerStep import OutputTriggerStep
    __doc__ = OutputTriggerStep.__doc__
    if kwds:
        return OutputTriggerStep(**kwds)
    return OutputTriggerStep


@pylith.foundry(tip="Output trigger time")
def time(**kwds):
    from .OutputTriggerTime import OutputTriggerTime
    __doc__ = OutputTriggerTime.__doc__
    if kwds:
        return OutputTriggerTime(**kwds)
    return OutputTriggerTime
