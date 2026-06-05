# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================

import graphene

import pylith

from .Version import Version


class Query(graphene.ObjectType):
    """The top level query."""

    # server version info
    version = graphene.Field(Version, required=True)

    # the resolvers
    @staticmethod
    def resolve_version(root, info, **kwds):
        """Report the PyLith version."""
        major, minor, micro = pylith.version()
        return Version(major=major, minor=minor, micro=micro, revision="")
