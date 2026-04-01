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


@pylith.foundry(tip="Quasistatic elasticity scale")
def quasistatic_elasticity():
    try:
        from .QuasistaticElasticity import QuasistaticElasticity
    except ImportError:
        return
    __doc__ = QuasistaticElasticity.__doc__
    return QuasistaticElasticity


@pylith.foundry(tip="Dynamic elasticity scale")
def dynamic_elasticity():
    try:
        from .DynamicElasticity import DynamicElasticity
    except ImportError:
        return
    __doc__ = DynamicElasticity.__doc__
    return DynamicElasticity


@pylith.foundry(tip="Quasistatic poroelasticity scale")
def quasistatic_poroelasticity():
    try:
        from .QuasistaticPoroelasticity import QuasistaticPoroelasticity
    except ImportError:
        return
    __doc__ = QuasistaticPoroelasticity.__doc__
    return QuasistaticPoroelasticity
