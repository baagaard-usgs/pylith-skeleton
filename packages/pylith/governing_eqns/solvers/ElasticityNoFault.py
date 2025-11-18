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

from ...solvers import SolverPetsc


class Elasticity(SolverPetsc, family="pylith.governing_eqns.solvers.elasticity_nofault"):
    """Solver for elasticity governing equation without a fault."""

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement ElasticityNoFault.__init__(). Pass parameters to C++.",
            )
        )
        todo.log()
