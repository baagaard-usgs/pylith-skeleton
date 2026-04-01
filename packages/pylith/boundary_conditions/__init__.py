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
def dirichlet():
    try:
        from .Dirichlet import Dirichlet
    except ImportError:
        return
    __doc__ = Dirichlet.__doc__
    return Dirichlet


@pylith.foundry(tip="Neumann boundary condition")
def neumann():
    try:
        from .Neumann import Neumann
    except ImportError:
        return
    __doc__ = Neumann.__doc__
    return Neumann
