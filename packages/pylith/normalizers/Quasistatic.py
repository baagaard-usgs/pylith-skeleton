import journal
import pyre

from pyre.units.length import meter
from pyre.units.time import year
from pyre.units.pressure import MPa
from pyre.units.mass import kilogram

from .Normalizer import Normalizer


class Quasistatic(
    pyre.component, family="pylith.normalizers.quasistatic", implements=Normalizer
):
    """Nondimensionaler for quasistatic problems."""

    length_scale = pyre.properties.dimensional(default=1.0 * meter)
    length_scale.doc = "Length scale for nondimensionalization."

    time_scale = pyre.properties.dimensional(default=1.0 * year)
    time_scale.doc = "Time scale for nondimensionalization."

    pressure_scale = pyre.properties.dimensional(default=10.0 * MPa)
    pressure_scale.doc = "Pressure scale for nondimensionalization."

    @pyre.export
    def display(self):
        """Display my scales."""
        channel = journal.info("application-flow")
        channel.line("Scales for nondimensionalization:")
        channel.line(f"  Length scale: {self.length_scale}")
        channel.line(f"  Time scale: {self.time_scale}")
        channel.line(f"  Pressure scale: {self.pressure_scale}")
        channel.log()
