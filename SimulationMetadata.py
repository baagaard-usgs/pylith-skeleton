import pyre

from Metadata import Metadata


class SimulationMetadata(pyre.component, family="pylith.metadata.simulationmetadata", implements=Metadata):
    """Simulation metadata."""

    author = pyre.properties.str()
    author.doc = "Author of simulation."

    description = pyre.properties.str()
    description.doc = "Description of simulation."

    @pyre.export
    def display(self):
        """Display my metadata."""
        print("Simulation Metadata")
        print(f"  Author: {self.author}")
        print(f"  Description: {self.description}")
        print("")
