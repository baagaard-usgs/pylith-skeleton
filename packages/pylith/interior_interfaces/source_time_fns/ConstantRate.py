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

from .SourceTimeFn import SourceTimeFnBase


class ConstantRate(SourceTimeFnBase, family="pylith.interior_interfaces.source_time_fns.constant_rate"):
    """ConstantRate source time function."""

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement ConstrantRate.__init__(). Pass parameters to C++.",
            )
        )
        todo.log()
