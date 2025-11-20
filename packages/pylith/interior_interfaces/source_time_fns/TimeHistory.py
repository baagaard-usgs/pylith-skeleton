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

from .SourceTimeFnBase import SourceTimeFnBase


class TimeHistory(SourceTimeFnBase, family="pylith.interior_interfaces.source_time_fns.time_history"):
    """TimeHistory source time function."""

    # time_history = db_time_history()
    # time_history.doc = "Time history."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement TimeHistory.__init__(). Pass parameters to C++.",
            )
        )
        todo.log()
