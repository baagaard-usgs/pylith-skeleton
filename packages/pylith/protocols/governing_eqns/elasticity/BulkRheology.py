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


class BulkRheology(pylith.protocol, family="pylith.governing_eqns.elasticity_eqn.bulk_rheologies"):
    """Protocol declarator for elasticity bulk rheologies."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {BulkRheology} implementation"""
        from ....governing_eqns.elasticity_eqn.bulk_rheologies import isotropic_linear

        return isotropic_linear
