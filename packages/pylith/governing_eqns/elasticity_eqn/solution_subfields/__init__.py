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


@pylith.foundry(tip="Solution subfields no fault")
def nofault():
    try:
        from .SubfieldsNoFault import SubfieldsNoFault
    except ImportError:
        return
    __doc__ = SubfieldsNoFault.__doc__
    return SubfieldsNoFault


@pylith.foundry(tip="Solution subfields fault")
def fault():
    try:
        from .SubfieldsFault import SubfieldsFault
    except ImportError:
        return
    __doc__ = SubfieldsFault.__doc__
    return SubfieldsFault
