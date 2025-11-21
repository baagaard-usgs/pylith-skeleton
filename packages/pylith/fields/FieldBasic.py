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

from ..protocols import field


class FieldBasic(pylith.component, implements=field, family="pylith.fields.basic"):
    """Basic Field."""

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        lines = [
            f"{self}",
            f"subfields={self.subfields}",
        ]
        lines += [f"    - {subfield.pyre_name}" for subfield in self.subfields]
        info.report(lines)
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement FieldBasic.__init__(). Pass parameters to C++.",))
        todo.log()
