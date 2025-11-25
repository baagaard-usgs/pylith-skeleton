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

from ....protocols import field
from ....protocols.fields import subfield, group
from ....fields import subfields, groups

from .ElasticityRheology import ElasticityRheology
from .ElasticityRheology import AuxiliarySubfields as AuxiliaryBase
from .ElasticityRheology import DerivedSubfields as DerivedBase


class AuxiliarySubfields(
    AuxiliaryBase,
    family="pylith.materials.elasticity.rheologies.isotropic_linear.auxiliary_subfields",
):
    """Auxiliary subfields for the isotropic linear bulk rheology."""

    shear_modulus = subfield(default=subfields.basic)
    shear_modulus.doc = "Shear modulus."

    bulk_modulus = subfield(default=subfields.basic)
    bulk_modulus.doc = "Bulk modulus."

    reference_state = group(default=groups.reference_state)
    reference_state.doc = "Reference state (optional)."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"shear modulus = {self.shear_modulus}",
                f"bulk modulus = {self.bulk_modulus}",
                f"reference state = {self.reference_state}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement IsotropicLinear.__init__(). Pass parameters to C++.",))
        todo.log()


class DerivedSubfields(
    DerivedBase,
    family="pylith.materials.elasticity.rheologies.isotropic_linear.derived_subfields",
):
    """Derived subfields for the isotropic linear bulk rheology."""

    cauchy_stress = subfield(default=subfields.optional)
    cauchy_stress.doc = "Cauchy stress (optional)."

    cauchy_strain = subfield(default=subfields.optional)
    cauchy_strain.doc = "Cauchy strain (optional)."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"{self.cauchy_stress}",
                f"{self.cauchy_strain}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report((f"Implement DerivedSubfields.__init__(). Pass parameters to C++.",))
        todo.log()


class IsotropicLinear(
    ElasticityRheology,
    family="pylith.governing_eqns.elasticity_eqn.bulk_rheologies.isotropic_linear",
):
    """Isotropic linear bulk rheology for elasticity."""

    auxiliary_subfields = field(default=AuxiliarySubfields)
    auxiliary_subfields.doc = "Rheology-specific material parameters."

    derived_subfields = field(default=DerivedSubfields)
    derived_subfields.doc = "Rheology-specific output subfields derived from solution and bulk rheology."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"auxiliary subfields = {self.auxiliary_subfields}",
                f"derived subfields = {self.derived_subfields}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement ElasticityRheology.__init__(). Pass parameters to C++.",))
        todo.log()
