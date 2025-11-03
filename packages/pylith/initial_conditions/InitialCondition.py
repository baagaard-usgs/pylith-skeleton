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


class InitialCondition(pylith.protocol, family="pylith.initial_conditions"):
    """Protocol declarator for initial conditions."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {InitialCondition} implementation"""
        from .InitialConditionDomain import InitialConditionDomain

        return InitialConditionDomain


class InitialConditionBase(pylith.component, implements=InitialCondition):
    """Base class for initial conditions."""

    subfields = pylith.properties.list(schema=pylith.properties.str(), default=["displacement"])
    subfields.doc = "Names of solution subfields for initial condition."

    # db = spatialdb.spatial_database(default=spatialdb.simpledb)
    # db.doc = "Spatial database with values for initial condition."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.warning(":TODO:")
        todo.report(
            (
                "Implement Dirichlet time_history attribute. Requires spatialdata.",
                "Implement Dirichlet.__init__(). Pass parameters to C++.",
                f"subfields={self.subfields}",
            )
        )
        todo.log()
