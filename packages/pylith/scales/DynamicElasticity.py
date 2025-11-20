# =================================================================================================
# This code is part of SpatialData, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/spatialdata).
#
# Copyright (c) 2010-2025, University of California, Davis and the SpatialData Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import pyre
from pyre.units.length import meter, km
from pyre.units.time import second
from pyre.units.mass import kg


import pylith

from .ScalesBase import ScalesBase


class DynamicElasticity(ScalesBase, family="pylith.scales.dynamic_elasticity"):
    """Convenience object for nondimensionalizing dynamic elasticity problems."""

    length_scale = pylith.properties.dimensional(default=100.0 * km)
    length_scale.validators = pyre.constraints.isGreater(value=0.0 * meter)
    length_scale.doc = "Length scale in boundary value problem (size of feature controlling displacement)."

    displacement_scale = pylith.properties.dimensional(default=1.0 * meter)
    displacement_scale.validators = pyre.constraints.isGreater(value=0.0 * meter)
    displacement_scale.doc = "Nominal displacement scale in boundary value problem."

    density = pylith.properties.dimensional(default=2500.0 * kg / meter**3)
    density.validators = pyre.constraints.isGreater(value=0.0 * kg / meter**3)
    density.doc = "Nominal density in boundary value problem."

    shear_wave_speed = pylith.properties.dimensional(default=3.0 * km / second)
    shear_wave_speed.validators = pyre.constraints.isGreater(value=0.0 * km / second)
    shear_wave_speed.doc = "Nominal shear wave speed in boundary value problem."

    # PUBLIC METHODS /////////////////////////////////////////////////////

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        rigidity_scale = self.density * self.shear_wave_speed * 2
        time_scale = self.length_scale / self.shear_wave_speed

        self.setLengthScale(self.length_scale)
        self.setDisplacementScale(self.displacement_scale)
        self.setRigidityScale(rigidity_scale)
        self.setTimeScale(time_scale)
