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

from ...protocols import field
from ...protocols.fields import subfield
from ...fields import subfields


class AuxiliarySubfields(
    pylith.component,
    implements=field,
    family="pylith.interior_interfaces.source_time_fns.constant_rate.auxiliary_subfields",
):
    """Auxiliary subfields for the constant rate source time function."""

    initiation_time = subfield(default=subfields.basic)
    initiation_time.doc = "Initiation time."

    slip_rate = subfield(default=subfields.basic)
    slip_rate.doc = "Slip rate."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory().initialization()
        info.report(
            (
                f"{self}",
                f"initiation time = {self.initiation_time}",
                f"slip rate = {self.slip_rate}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory().todo()
        todo.report(("Implement AuxiliarySubfields.__init__(). Pass parameters to C++.",))
        todo.log()


class ConstantRate(SourceTimeFnBase, family="pylith.interior_interfaces.source_time_fns.constant_rate"):
    """ConstantRate source time function."""

    auxiliary_field = field(default=AuxiliarySubfields)
    auxiliary_field.doc = "Auxiliary field with the constant rate source time function parameters."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.debug_factory().todo()
        todo.report(
            (
                f"{self}",
                "Implement ConstrantRate.__init__(). Pass parameters to C++.",
            )
        )
        todo.log()
