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
def ascii(**kwds):
    from .MeshIOAscii import MeshIOAscii
    __doc__ = MeshIOAscii.__doc__
    if kwds:
        return MeshIOAscii(**kwds)
    return MeshIOAscii


@pylith.foundry(tip="Cubit mesh I/O")
def cubit(**kwds):
    from .MeshIOCubit import MeshIOCubit
    __doc__ = MeshIOCubit.__doc__
    if kwds:
        return MeshIOCubit(**kwds)
    return MeshIOCubit


@pylith.foundry(tip="PETSc mesh I/O")
def petsc(**kwds):
    from .MeshIOPetsc import MeshIOPetsc
    __doc__ = MeshIOPetsc.__doc__
    if kwds:
        return MeshIOPetsc(**kwds)
    return MeshIOPetsc
