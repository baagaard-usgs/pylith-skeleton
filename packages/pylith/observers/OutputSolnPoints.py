# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import pylith


from .OutputObserver import OutputObserver


class OutputSolnPoints(OutputObserver, family="pylith.observers.solution_points"):
    """Output of solution over given points specified in a file."""

    filename = pylith.properties.uri(default=None)
    filename.doc = "URI with list of points."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"filename = {self.filename}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement OutputSolnPoints.__init__(). Pass parameters to C++.",))
        todo.log()
