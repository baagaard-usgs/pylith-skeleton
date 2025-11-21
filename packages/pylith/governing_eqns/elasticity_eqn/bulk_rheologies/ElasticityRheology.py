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

from .... import protocols
from .... import observers
from ....protocols.fields import subfield
from ....fields import subfields

from ....protocols.governing_eqns.elasticity import bulk_rheology


class AuxiliarySubfields(pylith.component, implements=protocols.field):

    density = subfield(default=subfields.basic)
    density.doc = "Mass density."

    body_force = subfield(default=subfields.optional)
    body_force.doc = "Body force."

    gravitational_acceleration = subfield(default=subfields.optional)
    gravitational_acceleration.doc = "Gravitational acceleration."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"density = {self.density}",
                f"body force = {self.body_force}",
                f"gravitional acceleration = {self.gravitational_acceleration}",
            )
        )

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement AuxiliarySubfields.__init__(). Pass parameters to C++.",))
        todo.log()


class DerivedSubfields(pylith.component, implements=protocols.field):
    pass


class ElasticityRheology(pylith.component, implements=bulk_rheology):

    label_name = pylith.properties.str(default=None)
    label_name.doc = "Name of label identifying boundary ()name of physical group in Gmsh files."

    label_value = pylith.properties.int(default=1)
    label_value.doc = "Value of label identifying boundary (tag of physical group in Gmsh files)."

    observers = pylith.properties.list(schema=protocols.observer(default=observers.output_physics))
    observers.doc = "Observer of material state."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"label name = {self.label_name}",
                f"label value = {self.label_value}",
                f"observers = {self.observers}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement MaterialBase.__init__(). Pass parameters to C++.",))
        todo.log()
