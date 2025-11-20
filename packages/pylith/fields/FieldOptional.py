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

# from ..protocols.fields import subfield


class FieldOptional(pylith.component, implements=field, family="pylith.fields.optional"):
    """Field with required and optional subfields."""

    # # :TODO: Convert to dict
    # required = pylith.properties.list(schema=subfield())
    # required.doc = "Required subfields in field."

    # # :TODO: Convert to dict
    # optional = pylith.properties.list(schema=group())
    # optional.doc = "Optional subfields in field."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement FieldOptional.__init__(). Pass parameters to C++.",
                f"required={self.required}",
                f"optional={self.optional}",
            )
        )
        todo.log()
