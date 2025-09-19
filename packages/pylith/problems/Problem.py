import pyre
import journal


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


class ProblemBase(pyre.component, implements=Problem):
    from pylith.boundary_conditions import boundary_condition, dirichlet
    from pylith.materials import material, elasticity
    from pylith.normalizers import normalizer as normalizer_scales

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

    normalizer = normalizer_scales()
    normalizer.doc = "Scales for nondimensionalization."

    @pyre.export
    def initialize(self):
        """Initialize the problem."""
        self.info_flow = journal.info("application-flow", detail=1)
        self.info_flow.log(
            f"Initializing problem '{self.pyre_name}' with {len(self.materials)} materials and {len(self.boundary_conditions)} boundary conditions."
        )

        for mat in self.materials:
            mat.initialize()

        for bc in self.boundary_conditions:
            bc.initialize()

    @pyre.export
    def solve(self):
        raise NotImplementedError(
            f"class '{type(self).__name__}' must implement 'Problem.solve()'"
        )
