# -*- coding: utf-8 -*-


# externals
import graphene

# support
import pylith

# types
from .Version import Version
from .journal import JournalChannel, channels


# the query
class Query(graphene.ObjectType):
    """
    The top level query
    """

    # the known queries
    # server version info
    version = graphene.Field(Version, required=True)
    # the journal channels the GUI offers
    journal = graphene.List(graphene.NonNull(JournalChannel), required=True)

    # the resolvers

    # version
    @staticmethod
    def resolve_version(root, info):
        """
        Build and return the server version
        """
        # supply the context for the {version} resolution
        return pylith.meta

    # journal
    @staticmethod
    def resolve_journal(root, info):
        """
        List the journal channels the GUI offers, from {pylith_app.yaml}
        """
        # the roster the configuration defines
        return channels()


# end of file
