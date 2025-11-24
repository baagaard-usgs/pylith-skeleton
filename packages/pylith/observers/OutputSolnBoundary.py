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


class OutputSolnBoundary(OutputObserver, family="pylith.observers.solution_boundary"):
    """Output of the solution over a domain boundary."""

    label_name = pylith.properties.str(default=None)
    label_name.doc = "Name of label for patch."

    label_value = pylith.properties.str(default=1)
    label_value.doc = "Value of label for patch."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"label name = {self.label_name}",
                f"label value = {self.label_value}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement OutputSolnBoundary.__init__(). Pass parameters to C++.",))
        todo.log()
