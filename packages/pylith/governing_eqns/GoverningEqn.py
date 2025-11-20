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


class GoverningEqn(pylith.protocol, family="pylith.governing_eqns"):
    """Protocol declarator for governing equations." """

    @classmethod
    def pyre_default(cls, **kwds):
        """
        The default {GoverningEqn} implementation
        """
        from .elasticity_eqn import elasticity_eqn

        return elasticity_eqn
