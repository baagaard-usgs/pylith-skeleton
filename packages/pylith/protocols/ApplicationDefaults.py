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


class ApplicationDefaults(pylith.protocol, family="pylith.defaults"):
    """Protocol declarator for application-level defaults." """

    @classmethod
    def pyre_default(cls, **kwds):
        """
        The default {ApplicationDefaults} implementation
        """
        from ..defaults import simulation_defaults

        return simulation_defaults
