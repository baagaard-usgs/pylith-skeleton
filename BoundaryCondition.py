import pyre

from pyre.units.length import meter

class BoundaryCondition(pyre.protocol, family="pylith.boundary_conditions"):
    """Protocol declarator for materials.
    """

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {BoundaryCondition} implementation
        """
        return DirichletBC

    @pyre.provides
    def initialize(self):
        """Initialize material.
        """

    @pyre.provides
    def setState(self, t):
        """Set material state.
        """

        
class DirichletBC(pyre.component, implements=BoundaryCondition):
    """Dirichlet boundary condition.
    """

    value = pyre.properties.dimensional(default=1.0*meter)
    value.doc = "Boundary condition value."

    @pyre.export
    def initialize(self):
        """Initialize Dirichlet boundary condition.
        """
        print("Initializing Dirichlet boundary condition '{self.pyre_name}'...")

    @pyre.export
    def setState(self, t):
        """Set Dirichlet boundary condition state.
        """
        print("Setting Dirichlet boundary condition state '{self.pyre_name}'...")

        
class NeumannBC(pyre.component, implements=BoundaryCondition):
    """Neumann boundary condition.
    """

    traction = pyre.properties.array(default=(0,0,0))
    traction.doc = "Default Neumann boundary condition value."

    @pyre.export
    def initialize(self):
        """Initialize Neumann boundary condition.
        """
        print("Initializing Neumann boundary condition '{self.pyre_name}'...")

    @pyre.export
    def setState(self, t):
        """Set Neumann boundary condition state.
        """
        print("Setting Neumann boundary condition state '{self.pyre_name}'...")


# end of file
