# -*- coding: utf-8 -*-

# externals
import graphene

# query
from .Query import Query

# mutation
# from .Mutation import Mutation


# build the schema
schema = graphene.Schema(
    # supported operations
    query=Query,
    # mutation=Mutation,
)


# render the schema as SDL text; the single source of truth shared by the generated
# {ux/schema/pylith.gql} relay artifact, the {pylith schema sdl} panel, and the {/schema}
# server route
def sdl() -> str:
    """
    Render the {pylith} GraphQL schema as SDL text
    """
    # graphene emits canonical SDL when the schema is stringified
    return str(schema)


# end of file
