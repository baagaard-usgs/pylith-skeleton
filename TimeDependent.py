import pyre
from pyre.units.time import second

from Problem import Problem

from Material import Material, Elasticity
from BoundaryCondition import BoundaryCondition, DirichletBC


class TimeDependent(pyre.component, family="pylith.problems.timedependent", implements=Problem):
    """A time dependent problem.
    """

    start_time = pyre.properties.dimensional(default=0.0*second)
    start_time.doc = "Problem start time."

    end_time = pyre.properties.dimensional(default=10.0*second)
    end_time.doc = "Problem end time."

    time_step = pyre.properties.dimensional(default=1.0*second)
    time_step.doc = "Initial time step for solve."

    materials = pyre.properties.list(schema=Material(default=Elasticity))
    materials.doc = "Materials in problem."

    boundary_conditions = pyre.properties.list(schema=BoundaryCondition(default=DirichletBC))
    boundary_conditions.doc = "Boundary conditions"
    
    @pyre.export
    def initialize(self):
        """Initialize the problem.
        """
        print("\n".join(list(self.pyre_showConfiguration())))
        for material in self.materials:
            material.initialize()
        for bc in self.boundary_conditions:
            bc.initialize()
        
    @pyre.export
    def solve(self):
        """Solve the time-dependent problem.
        """
        t = self.start_time
        while t <= self.end_time:
            print(f"t={t}")
            for bc in self.boundary_conditions:
                bc.setState(t)
            for material in self.materials:
                material.computeState(t)
            t += self.time_step
        for material in self.materials:
            material.finalState(t)
        

# end of file
