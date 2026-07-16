# -*- coding: utf-8 -*-


# externals
import graphene


# the server version
class Version(graphene.ObjectType):
    """
    The server version
    """

    # the fields
    major = graphene.Int(required=True)
    minor = graphene.Int(required=True)
    micro = graphene.Int(required=True)
    revision = graphene.String(required=True)


# end of file
