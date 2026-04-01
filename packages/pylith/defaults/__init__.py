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


@pylith.foundry(tip="Simulation defaults")
def simulation_defaults():
    try:
        from .SimulationDefaults import SimulationDefaults
    except ImportError:
        return
    __doc__ = SimulationDefaults.__doc__
    return SimulationDefaults
