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


class InitialCondition(pylith.protocol, family="pylith.initial_conditions"):
    """Protocol declarator for initial conditions."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {InitialCondition} implementation"""
        from ..initial_conditions import domain

        return domain
