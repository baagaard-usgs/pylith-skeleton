# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
from .Scales import Scales as scales
from .QuasistaticElasticity import QuasistaticElasticity as quasistatic_elasticity
from .DynamicElasticity import DynamicElasticity as dynamic_elasticity
from .QuasistaticPoroelasticity import QuasistaticPoroelasticity as quasistatic_poroelasticity


def string_list():
    scales = (
        # base
        "length",
        "displacement",
        "rigidity",
        "time",
        "temperature",
        # derived
        "velocity",
        "acceleration",
        "strain",
        "stress",
        "density",
        "permeability",
        "viscosity",
    )
    return scales
