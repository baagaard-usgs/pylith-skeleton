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


@pylith.foundry(tip="Time dependent problem")
def time_dependent(**kwds):
    from .TimeDependent import TimeDependent
    __doc__ = TimeDependent.__doc__
    if kwds:
        return TimeDependent(**kwds)
    return TimeDependent


@pylith.foundry(tip="Greens functions problem")
def greens_fns(**kwds):
    from .GreensFns import GreensFns
    __doc__ = GreensFns.__doc__
    if kwds:
        return GreensFns(**kwds)
    return GreensFns
