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


@pylith.foundry(tip="PETSc discretization")
def petsc(**kwds):
    from .DiscretizationPetsc import DiscretizationPetsc
    __doc__ = DiscretizationPetsc.__doc__
    if kwds:
        return DiscretizationPetsc(**kwds)
    return DiscretizationPetsc
