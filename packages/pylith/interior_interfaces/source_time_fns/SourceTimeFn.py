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

from pylith import journal
from pylith.fields import field


class SourceTimeFn(pylith.protocol, family="pylith.interior_interfaces.source_time_fns"):
    """Protocol declarator for source time functions."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {SorceTimeFn} implementation"""
        from .Step import Step

        return Step


class SourceTimeFnBase(pylith.component, implements=SourceTimeFn):

    auxiliary_field = field()
    auxiliary_field.doc = "Auxiliary field with source time function parameters."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement SourceTimeFnBase.__init__(). Pass parameters to C++.",
                f"auxiliary field={self.auxiliary_field}",
            )
        )
        todo.log()
