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

from ...protocols import field

from ...protocols.interior_interfaces import source_time_fn


class SourceTimeFnBase(pylith.component, implements=source_time_fn):

    auxiliary_field_db = field()
    auxiliary_field_db.doc = "Spatial database for populating auxiliary field with source time function parameters."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.debug_factory().todo()
        todo.report(
            (
                f"{self}",
                "Implement SourceTimeFnBase.__init__(). Pass parameters to C++.",
                f"auxiliary field db = {self.auxiliary_field_db}",
            )
        )
        todo.log()
