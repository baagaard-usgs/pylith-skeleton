import pyre
from pyre.units.time import second

from Problem import ProblemBase


class TimeDependent(ProblemBase, family="pylith.problems.timedependent"):
    """A time dependent problem."""

    start_time = pyre.properties.dimensional(default=0.0 * second)
    start_time.doc = "Problem start time."

    end_time = pyre.properties.dimensional(default=10.0 * second)
    end_time.doc = "Problem end time."

    time_step = pyre.properties.dimensional(default=1.0 * second)
    time_step.doc = "Initial time step for solve."

    @pyre.export
    def solve(self):
        """Solve the time-dependent problem."""
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
