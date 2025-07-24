import pyre


class Problem(pyre.protocol, family="pylith.problems"):
    """Problem to solve."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {Problem} implementation"""
        from TimeDependent import TimeDependent

        return TimeDependent

    @pyre.provides
    def initialize(self):
        """Initialize the problem."""

    @pyre.provides
    def solve(self):
        """Solve problem."""


class ProblemBase(pyre.component):
    # from Material import Material, Elasticity
    from BoundaryCondition import BoundaryCondition
    from DirichletBC import DirichletBC

    # from Interface import Interface, Fault
    # from Normalizer import Normalizer

    # materials = pyre.properties.list(schema=Material(default=Elasticity))
    # materials.doc = "Materials in problem."

    boundary_conditions = pyre.properties.list(schema=BoundaryCondition(default=DirichletBC))
    boundary_conditions.doc = "Boundary conditions"

    # interfaces = pyre.properties.list(schema=Interface(default=Fault))
    # interfaces.doc = "Interfaces"

    # solution_observers = pyre.properties.list(schema=Observer(default=SolutionObserver))
    # solution_observers.doc = "Solution observers"

    # normalizer = Normalizer()

    @pyre.export
    def initialize(self):
        """Initialize the problem."""
        print("\n".join(list(self.pyre_showConfiguration())))
        # for material in self.materials:
        #    material.initialize()
        print(f"# bcs {len(self.boundary_conditions)}")
        for bc in self.boundary_conditions:
            bc.initialize()
