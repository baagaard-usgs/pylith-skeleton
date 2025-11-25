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

from ...protocols import fields


class OptionalBase(pylith.component, implements=fields.group):
    """OptionalSubfield in PETSc field."""

    enabled = pylith.properties.bool(default=False)
    enabled.doc = "Turn on/off use of group."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"alias = {self.alias}",
                f"enabled = {self.enabled}",
                f"discretization = {self.discretization}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement SubfieldOptional.__init__(). Pass parameters to C++.",))
        todo.log()
