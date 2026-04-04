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
    family="pylith.interior_interfaces.source_time_fns.brune.auxiliary_subfields",
):
    """Auxiliary subfields for the Brune source time function."""

    initiation_time = subfield(default=subfields.basic)
    initiation_time.doc = "Shear modulus."

    final_slip = subfield(default=subfields.basic)
    final_slip.doc = "Bulk modulus."

    rise_time = subfield(default=subfields.basic)
    rise_time.doc = "Bulk modulus."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory().initialization()
        info.report(
            (
                f"{self}",
                f"initiation time = {self.initiation_time}",
                f"final slip = {self.final_slip}",
                f"rise time = {self.rise_time}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory().todo()
        todo.report(("Implement AuxiliarySubfields.__init__(). Pass parameters to C++.",))
        todo.log()


class Brune(SourceTimeFnBase, family="pylith.interior_interfaces.source_time_fns.brune"):
    """Brune source time function."""

    auxiliary_field = field(default=AuxiliarySubfields)
    auxiliary_field.doc = "Auxiliary field with Brune source time function parameters."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.debug_factory().todo()
        todo.report(
            (
                f"{self}",
                "Implement Brune.__init__(). Pass parameters to C++.",
            )
        )
        todo.log()
