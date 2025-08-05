import pyre

from pylith.metadata import metadata as app_metadata

from pylith.problems import problem
from pylith.problems import time_dependent


class PyLithApp(pyre.application):
    """Application for running PyLith simulations."""

    metadata = app_metadata()
    metadata.doc = "Application metadata"

    problems = pyre.properties.list(
        schema=problem(default=time_dependent),
        default=[time_dependent(name="sim.time_dependent")],
    )
    problems.doc = "Problems to solve."

    @pyre.export
    def main(self, *args, **kwds):
        """
        Solve problem.
        """
        self.welcome()
        self.initialize()
        self.solve()
        return 0

    def welcome(self):
        """Show greetings from journals."""
        self.metadata.welcome()
        for a_problem in self.problems:
            a_problem.welcome()

    def initialize(self):
        """Initialize problems."""
        for a_problem in self.problems:
            a_problem.initialize()

    def solve(self):
        """Solve problems."""
        for a_problem in self.problems:
            a_problem.solve()
