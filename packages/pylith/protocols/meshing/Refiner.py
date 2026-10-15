# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2026 All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import pylith


class Refiner(pylith.protocol, family="pylith.meshing.refiners"):
    """Refine finite-element mesh."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {Refiner} implementation"""
        from ...meshing.refiners import uniform

        return uniform


# End of file
