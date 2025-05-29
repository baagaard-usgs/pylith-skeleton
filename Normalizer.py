import pyre

from pyre.units.length import kilometer, meter
from pyre.units.time import year
from pyre.units.pressure import megapascal
from pyre.units.mass import kilogram


class Normalizer(pyre.protocol, family="pylith.normalizer"):
    """Protocol declarator for normalizer." """

    @classmethod
    def pyre_default(cls, **kwds):
        """
        The default {Normalizer} implementation
        """
        return NormalizerQuasistatic

    @pyre.provides
    def display(self):
        """Display my scales."""


class NormalizerQuasistatic(pyre.component, family="pylith.normalizer.quasistatic", implements=Normalizer):
    """Nondimensionaler for quasistatic problems."""

    length_scale = pyre.properties.dimensional(default=1.0 * kilometer)
    length_scale.doc = "Length scale for nondimensionalization."

    time_scale = pyre.properties.dimensional(default=1.0 * year)
    time_scale.doc = "Time scale for nondimensionalization."

    pressure_scale = pyre.properties.dimensional(default=1.0 * megapascal)
    pressure_scale.doc = "Pressure scale for nondimensionalization."

    density_scale = pyre.properties.dimensional(default=1.0 * kilogram / meter**3)
    density_scale.doc = "Density scale for nondimensionalization."

    @pyre.export
    def display(self):
        """Display my scales."""
        print("Scales for nondimensionalization:")
        print(f"  Length scale: {self.length_scale}")
        print(f"  Time scale: {self.time_scale}")
        print(f"  Pressure scale: {self.pressure_scale}")
        print(f"  Density scale: {self.density_scale}")
