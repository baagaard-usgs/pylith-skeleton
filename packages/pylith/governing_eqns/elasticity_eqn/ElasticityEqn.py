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

from ... import interior_interfaces

from ..GoverningEqnBase import GoverningEqnBase

from . import solution_subfields as subfields
from . import bulk_rheologies


class ElasticityEqn(GoverningEqnBase, family="pylith.governing_eqns.elasticity"):
    """Elasticity governing equation."""

    solution_subfields = subfields.solution_subfields(default=subfields.nofault)
    solution_subfields.doc = "Solution subfields for elasticity equation."

    materials = pylith.properties.list(schema=bulk_rheologies.bulk_rheology())
    materials.doc = "Materials in boundary value problem."

    interior_interfaces = pylith.properties.list(schema=interior_interfaces.interior_interface())
    interior_interfaces.doc = "Interior interfaces (faults) in boundary value problem."

    # - gravity_field

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement ElasticityEqn.__init__(). Pass parameters to C++.",
                f"solution subfields={self.solution_subfields}",
                f"materials={self.materials}",
                f"interior interfaces={self.interior_interfaces}",
            )
        )
        todo.log()
