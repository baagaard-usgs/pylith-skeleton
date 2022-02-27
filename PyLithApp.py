#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pyre

class PyLithApp(pyre.application):
    # types
    from Metadata import Metadata
    from Problem import Problem
    from TimeDependent import TimeDependent

    metadata = Metadata()
    metadata.doc = "Simulation metadata"

    problems = pyre.properties.list(schema=Problem(default=TimeDependent), default=[TimeDependent(name="problem")])
    problems.doc = "Problem to solve."
    
    # interface
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


# end of file
