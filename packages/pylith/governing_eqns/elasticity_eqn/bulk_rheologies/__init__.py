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
def elasticity_rheology(**kwds):
    from .ElasticityRheology import ElasticityRheology
    __doc__ = ElasticityRheology.__doc__
    if kwds:
        return ElasticityRheology(**kwds)
    return ElasticityRheology


@pylith.foundry(tip="Isotropic linear rheology")
def isotropic_linear(**kwds):
    from .IsotropicLinear import IsotropicLinear
    __doc__ = IsotropicLinear.__doc__
    if kwds:
        return IsotropicLinear(**kwds)
    return IsotropicLinear
