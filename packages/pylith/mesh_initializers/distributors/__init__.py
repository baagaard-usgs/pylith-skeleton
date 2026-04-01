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


@pylith.foundry(tip="PETSc distributor")
def petsc():
    try:
        from .DistributorPetsc import DistributorPetsc
    except ImportError:
        return
    __doc__ = DistributorPetsc.__doc__
    return DistributorPetsc
