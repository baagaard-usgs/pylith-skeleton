# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================

import json
import traceback

import journal

from .. import gql


class GraphQL:
    """The resolver of GraphQL queries and mutations."""

    def respond(self, server, request, **kwds):
        """Resolve the {query} and generate a response for the client."""
        # assemble the raw payload
        raw = b"\n".join(request.payload)
        # if there is nothing there, respond with an empty document; should never happen
        if not raw:
            return server.documents.OK(server=server)

        # parse the {request} payload
        payload = json.loads(raw)
        # get the query and the variable bindings
        query = payload.get("query")
        variables = payload.get("variables")

        # make a fresh copy of my context and decorate it for this request
        context = dict(self.context)
        context["server"] = server
        context["request"] = request

        # display the {query} details, if the user cares to see
        channel = journal.debug("pylith.ux.graphql")
        if channel:
            channel.line("query:")
            for line in query.strip().splitlines():
                channel.line(f"    {line}")
            if variables:
                channel.line("  variables:")
                for key, value in variables.items():
                    channel.line(f"    {key}: {value}")
            channel.log()

        # execute the query
        result = self.schema.execute(query, context=context, variables=variables)

        # assemble the resulting document
        doc = {"data": result.data}

        # if something went wrong
        if result.errors:
            messages = []
            channel = journal.warning("pylith.ux.graphql")
            for error in result.errors:
                lines = str(error).splitlines()
                channel.line("graphql:")
                channel.indent()
                channel.report(report=lines)
                channel.outdent()
                messages.extend(lines)
                # get the original error
                original = error.original_error
                if original:
                    channel.line()
                    channel.line("python:")
                    channel.indent()
                    for entry in traceback.format_exception(original):
                        lines = entry.splitlines()
                        channel.report(report=lines)
                        messages.extend(lines)
                    channel.outdent()
                channel.log()
            doc["errors"] = [{"message": "\n".join(messages)}]

        # encode it using JSON and serve it
        return server.documents.JSON(server=server, value=doc)

    def __init__(self, plexus, dispatcher, **kwds):
        super().__init__(**kwds)
        # load my schema and attach it
        self.schema = gql.schema
        # initialize the execution context
        self.context = {
            "plexus": plexus,
            "dispatcher": dispatcher,
        }
        # make sure my error channel is not fatal
        journal.error("pylith.ux.graphql").fatal = False
