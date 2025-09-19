import pyre


class Features(pyre.protocol, family="pylith.metadata.features"):
    """Protocol declarator for metadata." """

    @classmethod
    def pyre_default(cls, **kwds):
        """
        The default {Features} implementation
        """
        from .Components import Components

        return Components
