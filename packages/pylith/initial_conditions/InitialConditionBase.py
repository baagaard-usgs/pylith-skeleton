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

from ..protocols import initial_condition


class InitialConditionBase(pylith.component, implements=initial_condition):
    """Base class for initial conditions."""

    subfields = pylith.properties.strings(default=["displacement"])
    subfields.doc = "Names of solution subfields for initial condition."

    # db = spatialdb.spatial_database(default=spatialdb.simpledb)
    # db.doc = "Spatial database with values for initial condition."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report((f"subfields={self.subfields}",))
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(
            (
                "Implement Dirichlet time_history attribute. Requires spatialdata.",
                "Implement Dirichlet.__init__(). Pass parameters to C++.",
            )
        )
        todo.log()
