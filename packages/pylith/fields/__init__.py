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
def basic(**kwds):
    from .FieldBasic import FieldBasic
    __doc__ = FieldBasic.__doc__
    if kwds:
        return FieldBasic(**kwds)
    return FieldBasic


@pylith.foundry(tip="Optional field")
def optional(**kwds):
    from .FieldOptional import FieldOptional
    __doc__ = FieldOptional.__doc__
    if kwds:
        return FieldOptional(**kwds)
    return FieldOptional
