import pyre

from pylith.utils import component


class Problem(pyre.protocol, family="pylith.problems"):
    """Problem to solve."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {Problem} implementation"""
        from .TimeDependent import TimeDependent

        return TimeDependent

    @pyre.provides
    def initialize(self):
        """Initialize the problem."""

    @pyre.provides
    def solve(self):
        """Solve problem."""


class ProblemBase(component):
    from pylith.boundary_conditions import boundary_condition, dirichlet
    from pylith.materials import material, elasticity

    materials = pyre.properties.list(schema=material(default=elasticity))
    materials.doc = "Materials in problem."

    boundary_conditions = pyre.properties.list(
        schema=boundary_condition(default=dirichlet)
    )
    boundary_conditions.doc = "Boundary conditions"

    # interfaces = pyre.properties.list(schema=Interface(default=Fault))
    # interfaces.doc = "Interfaces"

    # solution_observers = pyre.properties.list(schema=Observer(default=SolutionObserver))
    # solution_observers.doc = "Solution observers"

    # normalizer = Normalizer()

    @pyre.export
    def initialize(self):
        """Initialize the problem."""
        channel = self.info

        channel.log(f"# materials {len(self.materials)}")
        for mat in self.materials:
            mat.initialize()

        channel.log(f"# boundary conditions {len(self.boundary_conditions)}")
        for bc in self.boundary_conditions:
            bc.initialize()
