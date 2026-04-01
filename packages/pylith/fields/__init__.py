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


@pylith.foundry(tip="Basic field")
def basic():
    try:
        from .FieldBasic import FieldBasic
    except ImportError:
        return
    __doc__ = FieldBasic.__doc__
    return FieldBasic


@pylith.foundry(tip="Optional field")
def optional():
    try:
        from .FieldOptional import FieldOptional
    except ImportError:
        return
    __doc__ = FieldOptional.__doc__
    return FieldOptional
