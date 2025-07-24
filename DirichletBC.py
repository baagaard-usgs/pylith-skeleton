import pyre

from pyre.units.length import meter

from BoundaryCondition import BoundaryCondition


class DirichletBC(pyre.component, implements=BoundaryCondition):
    """Dirichlet boundary condition."""

    value = pyre.properties.dimensional(default=1.0 * meter)
    value.doc = "Boundary condition value."

    @pyre.export
    def initialize(self):
        """Initialize Dirichlet boundary condition."""
        print(f"Initializing Dirichlet boundary condition '{self.pyre_name}'...")

    @pyre.export
    def setState(self, t):
        """Set Dirichlet boundary condition state."""
        print(f"Setting Dirichlet boundary condition state '{self.pyre_name}' value={self.value}...")
