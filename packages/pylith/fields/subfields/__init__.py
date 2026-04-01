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


@pylith.foundry(tip="Basic subfield")
def basic():
    try:
        from .SubfieldBasic import SubfieldBasic
    except ImportError:
        return
    __doc__ = SubfieldBasic.__doc__
    return SubfieldBasic


@pylith.foundry(tip="Optional subfield")
def optional():
    try:
        from .SubfieldOptional import SubfieldOptional
    except ImportError:
        return
    __doc__ = SubfieldOptional.__doc__
    return SubfieldOptional
