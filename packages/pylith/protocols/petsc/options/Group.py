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


class Group(pylith.protocol, family="pylith.petsc.options"):
    """Protocol declarator for group of PETSc options." """

    @classmethod
    def pyre_default(cls, **kwds):
        """
        The default {Group} implementation
        """
        from ....petsc.options.groups import group_list

        return group_list
