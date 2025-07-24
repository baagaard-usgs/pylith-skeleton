import pyre


class BoundaryCondition(pyre.protocol, family="pylith.boundary_condition"):
    """Protocol declarator for materials."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {BoundaryCondition} implementation"""
        from DirichletBC import DirichletBC

        return DirichletBC

    @pyre.provides
    def initialize(self):
        """Initialize boundary condition."""

    @pyre.provides
    def setState(self, t):
        """Set boundary condition state."""
