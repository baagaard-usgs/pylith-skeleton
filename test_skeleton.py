#!/usr/bin/env python3

import pyre
import journal


class Metadata(pyre.protocol, family="pylith.metadata"):
    """Protocol declarator for metadata." """

    @classmethod
    def pyre_default(cls, **kwds):
        """
        The default {Shape} implementation
        """
        return SimulationMetadata

    @pyre.provides
    def display(self):
        """Display my metadata."""


class SimulationMetadata(
    pyre.component, family="pylith.metadata.simulation", implements=Metadata
):
    """Simulation metadata."""

    author = pyre.properties.str()
    author.doc = "Author of simulation."

    description = pyre.properties.str()
    description.doc = "Description of simulation."

    info = None

    def init(self):
        self.info = journal.info(self.pyre_name)

    @pyre.export
    def display(self):
        """Display my metadata."""
        channel = self.info
        channel.line("Hello from {!r}".format(self.pyre_name))
        channel.line("Simulation metadata")
        channel.indent()
        channel.line("Author: {!r}".format(self.author))
        channel.line("Description: {!r}".format(self.description))
        channel.outdent()
        channel.log()


class PyLithApp(pyre.application):

    metadata = Metadata()
    metadata.doc = "Simulation metadata"

    @pyre.export
    def main(self, *args, **kwds):
        """
        Solve problem.
        """
        self.metadata.init()
        self.metadata.display()
        return 0


if __name__ == "__main__":
    name = pyre.executive.nameserver.get(name="sim", default="sim")
    app = PyLithApp(name=name)

    # Print out the application configuration
    channel = app.info
    channel.chronicler.decor = 3
    channel.line("application {!r}".format(app.pyre_name))
    channel.line("  metadata: {!r}".format(app.metadata.pyre_family()))
    channel.log()

    # Questions:
    # 1. How do I find out all of the command line options (--config, etc).
    # 2. In using the executive to get the application name, how does the user set the name (e.g., from the command line)?
    #   name = pyre.executive.nameserver.get(name="sim", default="sim")
    #   app = PyLithApp(name=name)
    # 3. What is a good way to print the full configuration hierarchy?
    # 4. How do I pass multiple configuration files (CFG, YAML) files as command line arguments? --config=FILENAME1,FILENAME2?
    # 5. How do I run the application on 2 processes using MPI?
    #   ./test_skeleton.py --metadata.author=Joe --shell=mpi.mpirun
    #   pyre.components.exceptions.ResolutionError: could not resolve 'mpi.mpirun' into a component that implements protocol 'pyre.shells'
    # 6. How does the user control (activate/deactivate, decor value)the journal output (e.g., command line or YAML files)?
    # 7. Why is the journal output for SimulationMetadata decorated with 'sim' instead of 'sim.metadata'?

    status = app.run()
    raise SystemExit(status)
