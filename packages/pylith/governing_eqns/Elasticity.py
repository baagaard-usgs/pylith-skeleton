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
from pylith import materials
from pylith.interior_interfaces import interior_interface

from .GoverningEqn import GoverningEqnBase


class Elasticity(GoverningEqnBase, family="pylith.governing_eqns.elasticity"):
    """Elasticity governing equation."""

    # :TODO: Convert to dict or just use names?
    materials = pylith.properties.list(schema=materials.material(default=materials.elasticity))
    materials.doc = "Materials in boundary value problem."

    # :TODO: Convert to dict or just use names?
    interior_interfaces = pylith.properties.list(schema=interior_interface())
    interior_interfaces.doc = "Interior interfaces (faults) in boundary value problem."

    # - gravity_field

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement Elasticity.__init__(). Pass parameters to C++.",
                f"materials={self.materials}",
                f"interior interfaces={self.interior_interfaces}",
            )
        )
        todo.log()
