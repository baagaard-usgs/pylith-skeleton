# -*- Python -*-
# -*- coding: utf-8 -*-
#
# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2026, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================

# externals
import graphene

# support
import pylith

# types
from .Version import Version
from .About import About
from .journal import JournalChannel, channels
from .launch import Job, launcher

# the idle sentinel for a server that has not run anything yet
from pylith.apps.launch.Job import Job as JobRecord


# the query
class Query(graphene.ObjectType):
    """
    The top level query
    """

    # the known queries
    # server version info
    version = graphene.Field(Version, required=True)
    # server "about" info
    about = graphene.Field(About, required=True)
    # the journal channels the GUI offers
    journal = graphene.List(graphene.NonNull(JournalChannel), required=True)
    # the current launch job
    job = graphene.Field(Job, required=True)

    # the resolvers

    # version
    @staticmethod
    def resolve_version(root, info):
        """
        Build and return the server version
        """
        # supply the context for the {version} resolution
        return pylith.meta

    # about
    @staticmethod
    def resolve_about(root, info):
        """
        Build and return the server "about" information
        """
        # supply {pylith.meta} as the context for resolving the {About} fields
        return pylith.meta

    # journal
    @staticmethod
    def resolve_journal(root, info):
        """
        List the journal channels the GUI offers, from {pylith_app.yaml}
        """
        # the roster the configuration defines
        return channels()

    # job
    @staticmethod
    def resolve_job(root, info):
        """
        Report the current launch job, or an idle sentinel before anything has run
        """
        # reach the launcher the server owns
        backend = launcher(info)
        # if there is none, the server has not installed one; report an idle job
        if backend is None:
            # nothing has run
            return JobRecord.idle()
        # otherwise, report whatever the launcher holds
        return backend.current()


# end of file
