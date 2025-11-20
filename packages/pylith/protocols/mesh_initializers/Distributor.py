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


class Distributor(pylith.protocol, family="pylith.mesh_initializers.distributors"):
    """Partition and distribute the mesh."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {Distributor} implementation"""
        from ...mesh_initializers.distributors import petsc

        return petsc
