import pyre

from pylith.utils import component
from .Metadata import Metadata


class Simulation(component, family="pylith.metadata.simulation", implements=Metadata):
    """Simulation metadata."""

    author = pyre.properties.str()
    author.doc = "Author of simulation."

    description = pyre.properties.str()
    description.doc = "Description of simulation."
