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

from .... import observers
from ....fields import field, subfields

from .BulkRheology import BulkRheology


class AuxiliarySubfields(pylith.component, implements=field):

    density = subfields.subfield(default=subfields.basic)
    density.doc = "Mass density."

    body_force = subfields.subfield(default=subfields.optional)
    body_force.doc = "Body force."

    gravitational_acceleration = subfields.subfield(default=subfields.optional)
    gravitational_acceleration.doc = "Gravitational acceleration."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement AuxiliarySubfields.__init__(). Pass parameters to C++.",
                f"density = {self.density}",
                f"body force = {self.body_force}",
                f"gravitional acceleration = {self.gravitational_acceleration}",
            )
        )
        todo.log()


class DerivedSubfields(pylith.component, implements=field):
    pass


class ElasticityRheology(pylith.component, implements=BulkRheology):

    label_name = pylith.properties.str(default=None)
    label_name.doc = "Name of label identifying boundary ()name of physical group in Gmsh files."

    label_value = pylith.properties.int(default=1)
    label_value.doc = "Value of label identifying boundary (tag of physical group in Gmsh files)."

    observers = pylith.properties.list(schema=observers.observer(default=observers.output_physics))
    observers.doc = "Observer of material state."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement MaterialBase.__init__(). Pass parameters to C++.",
                f"label name={self.label_name}",
                f"label value={self.label_value}",
                f"observers={self.observers}",
            )
        )
        todo.log()
