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


@pylith.foundry(tip="PETSc reordering")
def petsc():
    try:
        from .ReorderingPetsc import ReorderingPetsc
    except ImportError:
        return
    __doc__ = ReorderingPetsc.__doc__
    return ReorderingPetsc
