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


@pylith.foundry(tip="Dirichlet boundary condition")
def dirichlet(**kwds):
    from .Dirichlet import Dirichlet
    __doc__ = Dirichlet.__doc__
    if kwds:
        return Dirichlet(**kwds)
    return Dirichlet


@pylith.foundry(tip="Neumann boundary condition")
def neumann(**kwds):
    from .Neumann import Neumann
    __doc__ = Neumann.__doc__
    if kwds:
        return Neumann(**kwds)
    return Neumann
