# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import pyre
from pyre.units.pressure import pascal, GPa
from pyre.units.length import meter, km
from pyre.units.time import year


import pylith

from .ScalesBase import ScalesBase


class QuasistaticElasticity(ScalesBase, family="pylith.scales.quasistatic_elasticity"):
    """Convenience object for nondimensionalizing quasi-static elasticity problems."""

    length_scale = pylith.properties.dimensional(default=100.0 * km)
    length_scale.validators = pyre.constraints.isGreater(value=0.0 * meter)
    length_scale.doc = "Length scale in boundary value problem (size of feature controlling displacement, fault)."

    displacement_scale = pylith.properties.dimensional(default=1.0 * meter)
    displacement_scale.validators = pyre.constraints.isGreater(value=0.0 * meter)
    displacement_scale.doc = "Nominal displacement scale in boundary value problem."

    shear_modulus = pylith.properties.dimensional(default=10.0 * GPa)
    shear_modulus.validators = pyre.constraints.isGreater(value=0.0 * pascal)
    shear_modulus.doc = "Nominal shear modulus in boundary value problem."

    time_scale = pylith.properties.dimensional(default=100.0 * year)
    time_scale.validators = pyre.constraints.isGreater(value=0.0 * year)
    time_scale.doc = "Time scale of boundary value problem (for example, viscoelastic relaxation time)."

    # PUBLIC METHODS /////////////////////////////////////////////////////

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        self.setLengthScale(self.length_scale)
        self.setDisplacementScale(self.displacement_scale)
        self.setRigidityScale(self.shear_modulus)
        self.setTimeScale(self.time_scale)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"length scale = {self.length_scale}",
                f"displacement scale = {self.displacement_scale}",
                f"nominal shear modulus = {self.shear_modulus}",
                f"time scale = {self.time_scale}",
            )
        )
        info.log()


# End of file
