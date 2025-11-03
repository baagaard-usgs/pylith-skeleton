# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import pyre

import pylith
from pylith import journal
from pylith.utils import constraints

from .Field import Field
from .subfields import subfield
from .optional import group


class FieldOptional(pyre.component, implements=Field, family="pylith.fields.optional"):
    """Field with required and optional subfields."""

    name = pylith.properties.str()
    name.validators = constraints.notEmptyString()
    name.doc = "Name of field."

    required_subfields = pylith.properties.list(schema=subfield())
    required_subfields.doc = "Required subfields in field."

    optional_subfields = pylith.properties.list(schema=group())
    optional_subfields.doc = "Optional subfields in field."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.warning(":TODO:")
        todo.report(
            (
                "Implement FieldOptional.__init__(). Pass parameters to C++.",
                f"name={self.name}",
                f"required_subfields={self.required_subfields}",
                f"optional_subfields={self.optional_subfields}",
            )
        )
        todo.log()
