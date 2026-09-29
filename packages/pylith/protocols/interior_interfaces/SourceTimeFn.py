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


class SourceTimeFn(pylith.protocol, family="pylith.interior_interfaces.source_time_fns"):
    """Protocol declarator for source time functions."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {SorceTimeFn} implementation"""
        from ...interior_interfaces.source_time_fns import step

        return step
