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

from .GoverningEqn import GoverningEqn as governing_eqn


@pylith.foundry(tip="Elasticity governing equation")
def elasticity():
    try:
        from .elasticity_eqn import elasticity_eqn
    except ImportError:
        return
    __doc__ = elasticity_eqn.__doc__
    return elasticity_eqn
