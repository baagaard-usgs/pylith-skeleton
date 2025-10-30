import pylith


class Defaults(pylith.protocol, family="pylith.defaults"):
    """Protocol declarator for defaults." """

    @classmethod
    def pyre_default(cls, **kwds):
        """
        The default {Defaults} implementation
        """
        from .SimulationDefaults import SimulationDefaults

        return SimulationDefaults
