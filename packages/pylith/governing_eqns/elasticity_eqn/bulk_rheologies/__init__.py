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


@pylith.foundry(tip="Elasticity rheology")
def elasticity_rheology():
    try:
        from .ElasticityRheology import ElasticityRheology
    except ImportError:
        return
    __doc__ = ElasticityRheology.__doc__
    return ElasticityRheology


@pylith.foundry(tip="Isotropic linear rheology")
def isotropic_linear():
    try:
        from .IsotropicLinear import IsotropicLinear
    except ImportError:
        return
    __doc__ = IsotropicLinear.__doc__
    return IsotropicLinear
