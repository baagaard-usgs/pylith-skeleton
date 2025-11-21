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

from .. import protocols

from .ProblemBase import ProblemBase


class GreensFns(
    ProblemBase,
    family="pylith.problems.greens_fns",
):
    """Problem for generating Green's functions."""

    # - fields
    # - sources

    progress_monitor = protocols.progress_monitor()
    progress_monitor.doc = "Monitor for reporting progress of simulation."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        # self.cxx = CxxTimeDependent()
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"progress monitor={self.progress_monitor}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement GreensFns.__init__(). Pass parameters to C++.",))
        todo.log()
