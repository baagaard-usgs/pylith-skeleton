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

from pylith.fields import Field, subfields


class DerivedSubfields(
    pylith.component, implements=Field, family="pylith.materials.elastic_rheologies.derived_subfields.isotropic_linear"
):

    cauchy_stress = subfields.subfield(default=subfields.cauchy_stress_optional)
    cauchy_stress.doc = "Cauchy stress (optional)."

    cauchy_strain = subfields.subfield(default=subfields.cauchy_strain_optional)
    cauchy_strain.doc = "Cauchy strain (optional)."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.warning(":TODO:")
        todo.report(
            (
                f"{self.pyre_name}",
                "Implement IsotropicLinear.__init__(). Pass parameters to C++.",
                f"{self.cauchy_stress}",
                f"{self.cauchy_strain}",
            )
        )
        todo.log()
