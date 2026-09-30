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


@pylith.foundry(tip="Simulation options")
def simulation_options(**kwds):
    from .SimulationOptions import SimulationOptions
    __doc__ = SimulationOptions.__doc__
    if kwds:
        return SimulationOptions(**kwds)
    return SimulationOptions


@pylith.foundry(tip="Solver options")
def solver_options(**kwds):
    from .SolverOptions import SolverOptions
    __doc__ = SolverOptions.__doc__
    if kwds:
        return SolverOptions(**kwds)
    return SolverOptions
