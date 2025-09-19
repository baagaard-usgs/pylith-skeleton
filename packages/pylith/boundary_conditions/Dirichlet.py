import journal
import pyre

from pyre.units.length import meter

from .BoundaryCondition import BoundaryCondition


class Dirichlet(
    pyre.component,
    family="pylith.boundary_conditions.dirichlet",
    implements=BoundaryCondition,
):
    """Dirichlet boundary condition."""

    value = pyre.properties.dimensional(default=1.0 * meter)
    value.doc = "Boundary condition value."

    @pyre.export
    def initialize(self):
        """Initialize Dirichlet boundary condition."""
        self.info_flow = journal.info("application-flow", detail=2)
        self.info_flow.log(
            f"Initializing Dirichlet boundary condition '{self.pyre_name}'."
        )

    @pyre.export
    def setState(self, t):
        """Set Dirichlet boundary condition state."""
        self.info_flow.log(
            f"Setting state for Dirichlet boundary condition '{self.pyre_name}', value={self.value}."
        )
