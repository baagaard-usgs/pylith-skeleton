import pyre

from pylith.utils import component
from .BoundaryCondition import BoundaryCondition


class Neumann(
    component,
    family="pylith.boundary_conditions.neumann",
    implements=BoundaryCondition,
):
    """Neumann boundary condition."""

    traction = pyre.properties.array(default=(0, 0, 0))
    traction.doc = "Default Neumann boundary condition value."

    @pyre.export
    def initialize(self):
        """Initialize Neumann boundary condition."""
        print("Initializing Neumann boundary condition '{self.pyre_name}'...")

    @pyre.export
    def setState(self, t):
        """Set Neumann boundary condition state."""
        print("Setting Neumann boundary condition state '{self.pyre_name}'...")
