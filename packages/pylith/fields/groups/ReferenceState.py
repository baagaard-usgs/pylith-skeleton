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


from ..subfields import basic


class ReferenceState(pylith.component, implements=fields.group, family="pylith.fields.groups.reference_state"):
    """Group of subfields associated with reference state."""

    enabled = pylith.properties.bool(default=False)
    enabled.doc = "Turn on/off use of group."

    reference_stress = fields.subfield(default=basic)
    reference_stress.doc = "Reference stress."

    reference_strain = fields.subfield(default=basic)
    reference_strain.doc = "Reference strain."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"enabled = {self.enabled}",
                f"reference stress = {self.reference_stress}",
                f"reference strain = {self.reference_strain}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement ReferenceState.__init__(). Pass parameters to C++.",))
        todo.log()
