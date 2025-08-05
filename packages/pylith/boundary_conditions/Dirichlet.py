import pyre

from pyre.units.length import meter

from pylith.utils import component
from .BoundaryCondition import BoundaryCondition


class Dirichlet(
    component,
    family="pylith.boundary_conditions.dirichlet",
    implements=BoundaryCondition,
):
    """Dirichlet boundary condition."""

    value = pyre.properties.dimensional(default=1.0 * meter)
    value.doc = "Boundary condition value."

    @pyre.export
    def initialize(self):
        """Initialize Dirichlet boundary condition."""
        self.info.log(
            "Initializing Dirichlet boundary condition {!r}...".format(self.pyre_name)
        )

    @pyre.export
    def setState(self, t):
        """Set Dirichlet boundary condition state."""
        self.info.log(
            "Setting Dirichlet boundary condition state {!r} value={}...".format(
                self.pyre_name, self.value
            )
        )
        self.info.log()
