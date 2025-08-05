import pyre


class Normalizer(pyre.protocol, family="pylith.normalizers"):
    """Protocol declarator for normalizer." """

    @classmethod
    def pyre_default(cls, **kwds):
        """
        The default {Normalizer} implementation
        """
        from .Quasistatic import Quasistatic

        return Quasistatic

    @pyre.provides
    def display(self):
        """Display my scales."""
