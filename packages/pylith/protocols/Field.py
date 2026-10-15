# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2026 All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import pylith


class Field(pylith.protocol, family="pylith.fields"):
    """Protocol declarator for field." """

    @classmethod
    def pyre_default(cls, **kwds):
        """
        The default {Defaults} implementation
        """
        from ..fields import basic

        return basic


# End of file
