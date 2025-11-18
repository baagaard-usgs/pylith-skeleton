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


class Scales(pylith.protocol, family="pylith.scales"):
    """Scales for nondimensionalization."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {Scales} implementation"""
        from .QuasistaticElasticity import QuasistaticElasticity

        return QuasistaticElasticity


class ScalesBase(pylith.component, implements=Scales):
    """
    Base class for nondimensionalizing problems.
    """

    # PUBLIC METHODS /////////////////////////////////////////////////////

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)
        # self.cxx = CxxScales()
        todo = pylith.journal.warning(":TODO:")
        todo.log("Implement Scales.__init__().")

    def setLengthScale(self, length):
        """
        Set length scale.
        """
        # self.cxx.setLengthScale(length.value)
        todo = pylith.journal.warning(":TODO:")
        todo.report(("Implement Scales.setLengthScale()", f"length scale={length}"))
        todo.log()

    def getLengthScale(self):
        """
        Get length scale.
        """
        from pyre.units.length import meter

        return self.cxx.getLengthScale(self) * meter

    def setDisplacementScale(self, displacement):
        """
        Set displacement scale.
        """
        # self.cxx.setDisplacementScale(displacement.value)
        todo = pylith.journal.warning(":TODO:")
        todo.report(("Implement Scales.setDisplacementScale()", f"displacement scale={displacement}"))
        todo.log()

    def getDisplacementScale(self):
        """
        Get displacement scale.
        """
        from pyre.units.length import meter

        return self.cxx.getDisplacementScale() * meter

    def setRigidityScale(self, rigidity):
        """
        Set pressure scale.
        """
        # self.cxx.setRigidityScale(rigidity.value)
        todo = pylith.journal.warning(":TODO:")
        todo.report(("Implement Scales.setRigidityScale()", f"rigidity scale={rigidity}"))
        todo.log()

    def getRigidityScale(self):
        """
        Get pressure scale.
        """
        from pyre.units.pressure import pascal

        return self.cxx.getRigidityScale() * pascal

    def setTimeScale(self, time):
        """
        Get time scale.
        """
        # self.cxx.setTimeScale(time.value)
        todo = pylith.journal.warning(":TODO:")
        todo.report(("Implement Scales.setTimeScale()", f"displacement scale={time}"))
        todo.log()

    def getTimeScale(self):
        """
        Get time scale.
        """
        from pyre.units.time import second

        return self.cxx.getTimeScale() * second

    def setTemperatureScale(self, temperature):
        """
        Get temperature scale.
        """
        self.cxx.setTemperatureScale(temperature.value)

    def getTemperatureScale(self):
        """
        Get temperature scale.
        """
        from pyre.units.temperature import kelvin

        return self.cxx.getTemperatureScale() * kelvin
