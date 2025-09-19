import pyre

from .Features import Features


class Components(
    pyre.component, family="pylith.metadata.components", implements=Features
):
    """Simulation features (to test nested components)."""

    one = pyre.properties.str()
    one.doc = "First component."

    two = pyre.properties.str()
    two.doc = "Second component."
