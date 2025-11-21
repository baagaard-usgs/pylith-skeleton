# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import pyre

import pylith

from ..protocols import progress_monitor


class ProgressMonitorBase(pylith.component, implements=progress_monitor):
    """Abstract base class for simulation progress monitors."""

    filename = pylith.properties.uri(default=None)
    filename.doc = "Name of output file."

    update_percent = pylith.properties.float(default=5.0)
    update_percent.validators = pyre.constraints.isPositive()
    update_percent.doc = "Frequency of progress updates (percent)."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"filename = {self.filename}",
                f"update percent = {self.update_percent}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement ProgressMonitorBase.__init__(). Pass parameters to C++.",))
        todo.log()
