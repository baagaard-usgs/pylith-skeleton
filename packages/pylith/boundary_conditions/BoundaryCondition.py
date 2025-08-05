import pyre


class BoundaryCondition(pyre.protocol, family="pylith.boundary_conditions"):
    """Protocol declarator for materials."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {BoundaryCondition} implementation"""
        from .Dirichlet import Dirichlet

        return Dirichlet

    @pyre.provides
    def initialize(self):
        """Initialize boundary condition."""

    @pyre.provides
    def setState(self, t):
        """Set boundary condition state."""
