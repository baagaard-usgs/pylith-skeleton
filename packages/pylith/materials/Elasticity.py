import journal
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
        self.info_flow = journal.info("application-flow", detail=2)
        self.info_flow.log(f"Initializing material '{self.pyre_name}'")

    @pyre.export
    def setState(self, t):
        """Set material state."""
        self.info_flow.log(f"Setting state for elasticity material '{self.pyre_name}'.")

    @pyre.export
    def computeState(self, t):
        """Compute material state."""
        self.info_flow.log(
            f"Computing state for elasticity material '{self.pyre_name}'."
        )
