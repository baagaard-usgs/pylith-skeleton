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
from pylith import fields
from pylith import observers
from pylith.utils import constraints


class Material(pylith.protocol, family="pylith.materials"):
    """Protocol declarator for materials."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {Material} implementation"""
        from .Elasticity import Elasticity

        return Elasticity


class MaterialBase(pylith.component, implements=Material):

    label_name = pylith.properties.str()
    label_name.validators = constraints.notEmptyString()
    label_name.doc = "Name of label identifying boundary ()name of physical group in Gmsh files."

    label_value = pylith.properties.int(default=1)
    label_value.doc = "Value of label identifying boundary (tag of physical group in Gmsh files)."

    auxiliary_subfields = fields.field(default=fields.optional)
    auxiliary_subfields.doc = "Subfields in auxiliary field with material parameters."

    derived_subfields = fields.field(default=fields.optional)
    derived_subfields.doc = "Output subfields derived from solution or auxiliary field."

    # :TODO: Convert to dict or just use names?
    observers = pylith.properties.list(schema=observers.observer(default=observers.output_physics))
    observers.doc = "Observer of material state."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        import pdb

        pdb.set_trace()

        todo = journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement MaterialBase.__init__(). Pass parameters to C++.",
                f"label name={self.label_name}",
                f"label value={self.label_value}",
                f"auxiliary subfields={self.auxiliary_subfields}",
                f"derived subfields={self.derived_subfields}",
                f"observers={self.observers}",
            )
        )
        todo.log()
