import pyre

class Problem(pyre.protocol, family="pylith.problems"):
    """Problem to solve.
    """

    @classmethod
    def pyre_default(cls, **kwds):
        """
        The default {Problem} implementation
        """
        from TimeDependent import TimeDependent
        return TimeDependent

    @pyre.provides
    def initialize(self):
        """
        Initialize the problem.
        """

    @pyre.provides
    def solve(self):
        """
        Solve problem.
        """


# end of file
