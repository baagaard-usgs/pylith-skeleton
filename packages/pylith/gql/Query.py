# -*- coding: utf-8 -*-


# externals
import graphene

# support
import pylith

# types
from .Version import Version


# the query
class Query(graphene.ObjectType):
    """
    The top level query
    """

    # the known queries
    # server version info
    version = graphene.Field(Version, required=True)

    # the resolvers

    # version
    @staticmethod
    def resolve_version(root, info):
        """
        Build and return the server version
        """
        # supply the context for the {version} resolution
        return pylith.meta


# end of file
