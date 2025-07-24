import pyre


class Metadata(pyre.protocol, family="pylith.metadata"):
    """Protocol declarator for metadata." """

    @classmethod
    def pyre_default(cls, **kwds):
        """
        The default {Shape} implementation
        """
        from SimulationMetadata import SimulationMetadata

        return SimulationMetadata

    @pyre.provides
    def display(self):
        """Display my metadata."""
