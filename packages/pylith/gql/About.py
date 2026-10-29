# -*- coding: utf-8 -*-

# externals
import graphene

# types
from .Version import Version


# the server "about" information
class About(graphene.ObjectType):
    """
    Descriptive information about the server
    """

    # the fields
    version = graphene.Field(Version, required=True)
    authors = graphene.String(required=True)
    copyright = graphene.String(required=True)

    # the resolvers

    # version
    @staticmethod
    def resolve_version(root, info):
        """
        Supply the context for resolving the nested {version}
        """
        # {root} is {pylith.meta}, whose flat attributes feed {Version}
        return root

    # authors
    @staticmethod
    def resolve_authors(root, info):
        """
        Return the author roster
        """
        # read the roster off {pylith.meta}
        return root.authors.strip()

    # copyright
    @staticmethod
    def resolve_copyright(root, info):
        """
        Return the copyright notice
        """
        # read the notice off {pylith.meta}
        return root.copyright.strip()


# End of file
