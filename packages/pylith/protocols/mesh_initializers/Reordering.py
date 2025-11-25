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


class Reordering(pylith.protocol, family="pylith.mesh_initializers.reorderings"):
    """Reorder a mesh."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {Reordring} implementation"""
        from ...mesh_initializers.reoderings import petsc

        return petsc
