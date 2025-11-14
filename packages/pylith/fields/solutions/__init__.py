# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================

from .Solution import Solution as solution
from .SolutionBasic import SolutionBasic as basic

from .. import subfields


def solution_class(name: str, subfields: dict):
    """Create class for subfield."""
    attributes = subfields | {"family": f"pylith.fields.solutions.{name}"}
    return type(name, (basic,), attributes)


# Elasticity
elasticity_nofault = solution_class(
    "elasticity_nofault",
    subfields={
        "displacement": subfields.subfield(default=subfields.displacement),
        "velocity": subfields.subfield(default=subfields.velocity),
    },
)
elasticity_fault = solution_class(
    "elasticity_fault",
    subfields={
        "displacement": subfields.subfield(default=subfields.displacement),
        "velocity": subfields.subfield(default=subfields.velocity),
        "lagrange_multiplier_fault": subfields.subfield(default=subfields.lagrange_multiplier_fault),
    },
)

# Incompressible elasticity
incompressible_elasticity_nofault = solution_class(
    "incompressible_elasticity_nofault",
    subfields={
        "displacement": subfields.subfield(default=subfields.displacement),
        "velocity": subfields.subfield(default=subfields.velocity),
        "pressure": subfields.subfield(default=subfields.pressure),
    },
)
