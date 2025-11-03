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

from .Group import Group
from ..subfields import subfield


class GroupList(pylith.component, implements=Group, family="pylith.fields.optional.group_list"):
    """PETSc options manager."""

    enabled = pylith.properties.bool()
    enabled.doc = "Use group of optional fields if True."

    subfields = pylith.properties.list(schema=subfield)
    subfields.doc = "List of subfields."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        self.enabled
        self.subfields

        todo = journal.warning(":TODO:")
        todo.report(
            (
                "Implement GroupList.__init__(). Pass parameters to C++.",
                f"enabled={self.enabled}",
                f"options={self.subfields}",
            )
        )
        todo.log()
