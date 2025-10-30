# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the SpatialData Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================

from pyre.units.length import km, meter
from pyre.units.time import year, second
from pyre.units.pressure import pascal
from pyre.units.mass import kg

# from ._scales import ElasticityScales as CxxElasticityScales


class ElasticityScales:
    """
    Nondimensionalization for elasticity related boundary value problems.
    """

    @staticmethod
    def setQuasistaticElasticity(scales, lengthScale=100.0 * km, timeScale=year):
        scales.cxx.setQuasistaticElasticity(scales, lengthScale.value, timeScale.value)

    @staticmethod
    def setDynamicElasticity(scales, lengthScale=100.0 * km, velocityScale=3.0 * km / second):
        scales.cxx.setDynamicElasticity(scales, lengthScale.value, velocityScale.value)

    @staticmethod
    def setQuasistaticPoroelasticity(
        scales,
        lengthScale=100.0 * km,
        permeability=1.0e-12 * meter**2,
        viscosity=1.0e-3 * pascal * second,
        rigidity=25.0e9 * pascal,
    ):
        scales.cxx.setQuasistaticPoroelasticity(
            lengthScale.value,
            permeability.value,
            viscosity.value,
            rigidity.value,
        )

    @staticmethod
    def computePoroelasticityTimeScale(viscosity, permeability, length, rigidity):
        timeScale = CxxElasticityScales.computePoroelasticityTimeScale(
            viscosity.value, permeability.value, length.value, rigidity.value
        )
        return timeScale * second

    @staticmethod
    def getStressScale(scales):
        return scales.cxx.getStressScale() * pascal

    @staticmethod
    def getFluidPressureScale(scales):
        return scales.cxx.getFluidPressureScale() * pascal

    @staticmethod
    def getStrainScale(scales):
        return scales.cxx.getStrainScale()

    @staticmethod
    def getBodyForceScale(scales):
        return scales.cxx.getBodyForceScale() * pascal / meter

    @staticmethod
    def getDensityScale(scales):
        return scales.cxx.getDensityScale() * kg / meter**3

    @staticmethod
    def getVelocityScale(scales):
        return scales.cxx.getVelocityScale() * meter / second

    @staticmethod
    def getAccelerationScale(scales):
        return scales.cxx.getAccelerationScale() * meter / second**2

    @staticmethod
    def getViscosityScale(scales):
        return scales.cxx.getViscosityScale() * pascal * second

    @staticmethod
    def getPermeabilityScale(scales):
        return scales.cxx.getPermeabilityScale() * meter**2


# End of file
