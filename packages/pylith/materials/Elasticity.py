# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
from pylith import journal

from .Material import MaterialBase
from .elasticity_rheologies import bulk_rheology


class Elasticity(MaterialBase, family="pylith.materials.elasticity"):
    """Elasticity material behavior."""

    rheology = bulk_rheology()
    rheology.doc = "Bulk rheology for elastic material."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement Elasticity.__init__(). Pass parameters to C++.",
                f"rheology={self.rheology}",
            )
        )
        todo.log()
