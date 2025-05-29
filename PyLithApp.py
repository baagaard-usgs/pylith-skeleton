import pyre


class PyLithApp(pyre.application):
    from Metadata import Metadata
    from Problem import Problem
    from TimeDependent import TimeDependent

    metadata = Metadata()
    metadata.doc = "Simulation metadata"

    problems = pyre.properties.list(schema=Problem(default=TimeDependent), default=[TimeDependent(name="problem")])
    problems.doc = "Problem to solve."

    @pyre.export
    def main(self):
        """
        Solve problem.
        """
        self.metadata.display()
        for problem in self.problems:
            problem.initialize()

        for problem in self.problems:
            problem.solve()
        return 0
