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
def quasistatic_elasticity(**kwds):
    from .QuasistaticElasticity import QuasistaticElasticity
    __doc__ = QuasistaticElasticity.__doc__
    if kwds:
        return QuasistaticElasticity(**kwds)
    return QuasistaticElasticity


@pylith.foundry(tip="Dynamic elasticity scale")
def dynamic_elasticity(**kwds):
    from .DynamicElasticity import DynamicElasticity
    __doc__ = DynamicElasticity.__doc__
    if kwds:
        return DynamicElasticity(**kwds)
    return DynamicElasticity


@pylith.foundry(tip="Quasistatic poroelasticity scale")
def quasistatic_poroelasticity(**kwds):
    from .QuasistaticPoroelasticity import QuasistaticPoroelasticity
    __doc__ = QuasistaticPoroelasticity.__doc__
    if kwds:
        return QuasistaticPoroelasticity(**kwds)
    return QuasistaticPoroelasticity
