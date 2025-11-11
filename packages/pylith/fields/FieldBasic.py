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


class FieldBasic(pyre.component, implements=Field, family="pylith.fields.basic"):
    """Basic Field."""

    # :TODO: Convert to dict
    subfields = pylith.properties.list(schema=subfield())
    subfields.doc = "Subfields in field."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement FieldBasic.__init__(). Pass parameters to C++.",
                f"subfields={self.subfields}",
            )
        )
        todo.log()
