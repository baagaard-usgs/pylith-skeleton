import pyre
from pyre.units.mass import kg
from pyre.units.time import s
from pyre.units.length import m

from Material import MaterialBase


class IncompressibleElasticity(MaterialBase, family="pylith.materials.incompressibleelasticity"):
    """Incompressible elastic material behavior."""

    density = pyre.properties.dimensional(default=3000 * kg / m**3)
    density.doc = "Mass density."

    vs = pyre.properties.dimensional(default=5200.0 * m / s)
    vs.doc = "S wave speed."

    @pyre.export
    def initialize(self):
        """Initialize material."""
        print(f"Incompressible elasticity material '{self.pyre_name}'")
        print("\n".join(list(self.pyre_showConfiguration())))

    @pyre.export
    def setState(self, t):
        """Set material state."""
        print(f"Setting state for incompressible elasticity material '{self.pyre_name}'...")

    @pyre.export
    def computeState(self, t):
        """Compute material state."""
        print(f"Computing state for incompressible elasticity material '{self.pyre_name}'...")

    @pyre.export
    def finalState(self, t):
        """Set material end state."""
        return


class Injector(pyre.component, family="pylith.injectors.material"):
    """Inject value into material state."""

    target = Material()
    target.doc = "Material to inject value into."

    value = pyre.properties.float(default=2.0)
    value.doc = "Value to inject."

    @pyre.export
    def setState(self):
        """Update state."""
        self.target.setState(self.value)


class Transfer(pyre.component, family="pylith.transfer.material", implements=(Observer, Injector)):
    """Transfer state from one object to another."""

    target = Material()
    target.doc = "Material to inject value into."

    def __init__(self, **kwds):
        """Constructor."""
        super().__init__(**kwds)
        self.t = None

    @pyre.export
    def update(self, t):
        """Update observer."""
        self.t = t
        self.setState()

    @pyre.export
    def setState(self):
        """Update state."""
        self.target.setState(self.t)
