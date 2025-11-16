# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================

from .Subfield import Subfield as subfield
from .SubfieldBasic import SubfieldBasic as basic


def default_components(name: str, vector_field_type: str):
    """Get default names of subfield components."""
    if vector_field_type == "scalar":
        names = None
    elif vector_field_type == "vector":
        names = [f"{name}_{v}" for v in ("x", "y", "z")]
    elif vector_field_type == "tensor":
        names = [f"{name}_{v}" for v in ("xx", "yy", "zz", "xy", "yz", "xz")]
    else:
        raise ValueError("No default components for vector field type '{vector_field_type}' in {name}.")
    return names


def subfield_class(name: str, scale: str, vector_field_type: str, components: str = None):
    """Create class for subfield."""
    attributes = {"name": name, "scale": scale, "vector_field_type": vector_field_type}
    if components is None:
        attributes["components"] = default_components(name=name, vector_field_type=vector_field_type)
    return type(name, (basic,), attributes)


# Solution subfields
displacement = subfield_class(name="displacement", scale="displacement", vector_field_type="vector")
velocity = subfield_class(name="velocity", scale="velocity", vector_field_type="vector")
lagrange_multiplier_fault = subfield_class(name="lagrange_multiplier_fault", scale="stress", vector_field_type="vector")
pressure = subfield_class(name="pressure", scale="stress", vector_field_type="scalar")
fluid_pressure = subfield_class(name="fluid_pressure", scale="stress", vector_field_type="scalar")
trace_strain = subfield_class(name="trace_strain", scale="strain", vector_field_type="scalar")

# Governing equation and material subfields
density = subfield_class(name="density", scale="density", vector_field_type="scalar")
shear_modulus = subfield_class(name="shear_modulus", scale="rigidity", vector_field_type="scalar")
bulk_modulus = subfield_class(name="bulk_modulus", scale="rigidity", vector_field_type="scalar")
body_force = subfield_class(name="body_force", scale="body_force", vector_field_type="vector")
gravitational_acceleration = subfield_class(
    name="gravitational_acceleration", scale="acceleration", vector_field_type="vector"
)

cauchy_stress = subfield_class(name="cauchy_stress", scale="stress", vector_field_type="tensor")
cauchy_strain = subfield_class(name="cauchy_strain", scale="strain", vector_field_type="tensor")
