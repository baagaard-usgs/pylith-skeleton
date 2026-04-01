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


@pylith.foundry(tip="Initial condition domain")
def domain():
    try:
        from .InitialConditionDomain import InitialConditionDomain
    except ImportError:
        return
    __doc__ = InitialConditionDomain.__doc__
    return InitialConditionDomain


@pylith.foundry(tip="Initial condition patch")
def patch():
    try:
        from .InitialConditionPatch import InitialConditionPatch
    except ImportError:
        return
    __doc__ = InitialConditionPatch.__doc__
    return InitialConditionPatch
