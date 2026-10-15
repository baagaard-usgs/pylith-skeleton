# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2026 All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import pylith


@pylith.foundry(tip="Solution subfields without a fault")
def no_fault(**kwds):
    from .SubfieldsNoFault import SubfieldsNoFault

    __doc__ = SubfieldsNoFault.__doc__
    if kwds:
        return SubfieldsNoFault(**kwds)
    return SubfieldsNoFault


@pylith.foundry(tip="Solution subfields fault")
def fault(**kwds):
    from .SubfieldsFault import SubfieldsFault

    __doc__ = SubfieldsFault.__doc__
    if kwds:
        return SubfieldsFault(**kwds)
    return SubfieldsFault


# End of file
