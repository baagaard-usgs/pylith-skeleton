import journal
import pyre

import pylith


class Run(pylith.shells.command, family="pyre.cli.run"):
    """Run the application."""

    @pyre.export(tip="generate completions candidates from a partial command line")
    def main(self, plexus, argv, **kwds):
        # :KLUDGE: set default journal parameters
        journal.decor(1)
        journal.detail(1)

        self.initialize(plexus)
        self.solve(plexus)
        return 0

    def initialize(self, app):
        """Initialize problems."""
        channel = journal.info("application-flow")
        channel.log("Initializing application")
        for problem in app.problems:
            problem.initialize()

    def solve(self, app):
        """Solve problems."""
        channel = journal.info("application-flow")
        channel.log("Solving problems")
        for problem in app.problems:
            problem.solve()
