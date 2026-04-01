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


@pylith.foundry(tip="ASCII mesh I/O")
def ascii():
    try:
        from .MeshIOAscii import MeshIOAscii
    except ImportError:
        return
    __doc__ = MeshIOAscii.__doc__
    return MeshIOAscii


@pylith.foundry(tip="Cubit mesh I/O")
def cubit():
    try:
        from .MeshIOCubit import MeshIOCubit
    except ImportError:
        return
    __doc__ = MeshIOCubit.__doc__
    return MeshIOCubit


@pylith.foundry(tip="PETSc mesh I/O")
def petsc():
    try:
        from .MeshIOPetsc import MeshIOPetsc
    except ImportError:
        return
    __doc__ = MeshIOPetsc.__doc__
    return MeshIOPetsc
