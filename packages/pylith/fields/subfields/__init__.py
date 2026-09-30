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
def basic(**kwds):
    from .SubfieldBasic import SubfieldBasic
    __doc__ = SubfieldBasic.__doc__
    if kwds:
        return SubfieldBasic(**kwds)
    return SubfieldBasic


@pylith.foundry(tip="Optional subfield")
def optional(**kwds):
    from .SubfieldOptional import SubfieldOptional
    __doc__ = SubfieldOptional.__doc__
    if kwds:
        return SubfieldOptional(**kwds)
    return SubfieldOptional
