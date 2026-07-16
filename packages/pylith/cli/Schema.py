# -*- coding: utf-8 -*-


# support
import pylith
from pylith import gql


# declaration
class Schema(pylith.shells.command, family="pylith.cli.schema"):
    """
    Export the qed GraphQL schema
    """

    # user configurable state
    stream = pylith.properties.ostream()
    stream.doc = "The file to write; stdout by default."

    # interface
    @pylith.export(tip="Render the GraphQL schema as SDL")
    def sdl(self, **kwds):
        """
        Render the schema as SDL and emit it to my {stream}
        """
        # render the schema body
        body = gql.sdl().strip()
        # assemble the document: preamble, a blank separator, the body, then the marker
        document = "\n".join([*self.preamble, "", "", body, "", "# end of file"])
        # write it out
        print(document, file=self.stream)
        # all done; report success
        return 0

    # the preamble rendered above the SDL body in the generated file
    preamble = (
        "# -*- graphql -*-",
        "#",
        "# GENERATED FILE -- do not edit by hand",
        "# regenerate with `pylith schema sdl`",
        "# source of truth: pylith.gql.sdl",
    )


# end of file
