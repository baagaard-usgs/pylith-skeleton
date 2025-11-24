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
from pyre.units.time import year, second

import pylith

from .ScalesBase import ScalesBase
from .ElasticityScales import ElasticityScales


class QuasistaticPoroelasticity(ScalesBase, family="pylith.scales.quasistatic_poroelasticity"):
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

    viscosity = pylith.properties.dimensional(default=0.001 * pascal * second)
    viscosity.validators = pyre.constraints.isGreater(value=0.0 * pascal)
    viscosity.doc = "Nominal fluid viscosity in boundary value problem."

    permeability = pylith.properties.dimensional(default=1.0e-13 * meter**2)
    permeability.validator = pyre.constraints.isGreater(value=0.0 * pascal)
    permeability.doc = "Nominal permeability in boundary value problem."

    # PUBLIC METHODS /////////////////////////////////////////////////////

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        ElasticityScales.setQuasistaticPoroelasticity(
            self,
            lengthScale=self.length_scale,
            rigidity=self.shear_modulus,
            viscosity=self.viscosity,
            permeability=self.permeability,
        )
        self.setDisplacementScale(self.displacement_scale)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"length scale = {self.length_scale}",
                f"displacement scale = {self.displacement_scale}",
                f"nominal shear modulus = {self.shear_modulus}",
                f"nominal viscosity = {self.viscosity}",
                f"nominal permeability = {self.permeability}",
            )
        )
        info.log()


# End of file
