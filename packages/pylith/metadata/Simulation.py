import pyre

from .Metadata import Metadata

from pylith.metadata import features as meta_features


class Simulation(
    pyre.component, family="pylith.metadata.simulation", implements=Metadata
):
    """Simulation metadata."""

    author = pyre.properties.str()
    author.doc = "Author of simulation."

    description = pyre.properties.str()
    description.doc = "Description of simulation."

    features = meta_features()
    features.doc = "Simulation features"
