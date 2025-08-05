import pyre


class Metadata(pyre.protocol, family="pylith.metadata"):
    """Protocol declarator for metadata." """

    @classmethod
    def pyre_default(cls, **kwds):
        """
        The default {Shape} implementation
        """
        from .Simulation import Simulation

        return Simulation
