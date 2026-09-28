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


@pylith.foundry(tip="Elasticity governing equation")
def elasticity(**kwds):
    from .Elasticity import Elasticity
    __doc__ = Elasticity.__doc__
    if kwds:
        return Elasticity(**kwds)
    return Elasticity
