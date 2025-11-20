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


class DataWriter(pylith.protocol, family="pylith.data_writers"):
    """Protocol declarator for data writers."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {DataWriter} implementation"""
        from ..data_writers import hdf5

        return hdf5
