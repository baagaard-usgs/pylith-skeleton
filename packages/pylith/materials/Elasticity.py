import pyre
from pyre.units.mass import kg
from pyre.units.time import s
from pyre.units.length import m

from .Material import MaterialBase


class Elasticity(MaterialBase, family="pylith.materials.elasticity"):
    """Elasticity material behavior."""

    density = pyre.properties.dimensional(default=3000 * kg / m**3)
    density.doc = "Mass density."

    vp = pyre.properties.dimensional(default=5200.0 * m / s)
    vp.doc = "P wave speed."

    vs = pyre.properties.dimensional(default=3000.0 * m / s)
    vs.doc = "S wave speed."

    @pyre.export
    def initialize(self):
        """Initialize material."""
        print(f"Elasticity material '{self.pyre_name}'")
        print("\n".join(list(self.pyre_showConfiguration())))

    @pyre.export
    def setState(self, t):
        """Set material state."""
        print(f"Setting state for elasticity material '{self.pyre_name}'...")

    @pyre.export
    def computeState(self, t):
        """Compute material state."""
        print(f"Computing state for elasticity material '{self.pyre_name}'...")
