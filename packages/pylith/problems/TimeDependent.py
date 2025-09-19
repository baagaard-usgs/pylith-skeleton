import journal
import pyre
from pyre.units.time import second

from .Problem import ProblemBase


class TimeDependent(
    ProblemBase,
    family="pylith.problems.time_dependent",
):
    """A time dependent problem."""

    start_time = pyre.properties.dimensional(default=0.0 * second)
    start_time.doc = "Problem start time."

    end_time = pyre.properties.dimensional(default=0.0 * second)
    end_time.doc = "Problem end time."

    time_step = pyre.properties.dimensional(default=1.0 * second)
    time_step.doc = "Initial time step for solve."

    @pyre.export
    def solve(self):
        """Solve the time-dependent problem."""
        t = self.start_time
        while t <= self.end_time:
            self.info_flow.log(f"Problem '{self.pyre_name}' solving at t={t}.")
            for bc in self.boundary_conditions:
                bc.setState(t)
            for mat in self.materials:
                mat.computeState(t)
            t += self.time_step

        for mat in self.materials:
            mat.finalState(t)
