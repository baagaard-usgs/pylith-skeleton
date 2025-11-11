import pyre
import journal

from pylith.metadata import metadata as app_metadata

from pylith.problems import problem
from pylith.problems import time_dependent


class PyLithApp(pyre.application):
    """Application for running PyLith simulations."""

    metadata = app_metadata()
    metadata.doc = "Application metadata"

    # :TODO: Convert to dict
    problems = pyre.properties.list(
        schema=problem(default=time_dependent),
        default=[time_dependent(name="problem")],
    )
    problems.doc = "Problems to solve."

    @pyre.export
    def main(self, *args, **kwds):
        """
        Solve problem.
        """
        self.initialize()
        self.solve()
        return 0

    def initialize(self):
        """Initialize problems."""
        channel = journal.info("application-flow")
        channel.log("Initializing application")
        for a_problem in self.problems:
            a_problem.initialize()

    def solve(self):
        """Solve problems."""
        channel = journal.info("application-flow")
        channel.log("Solving problems")
        for a_problem in self.problems:
            a_problem.solve()
