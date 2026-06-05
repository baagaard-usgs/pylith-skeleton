# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================

import re
import signal

import journal

from .GraphQL import GraphQL


class Dispatcher:
    """The handler of web requests.

    P0 routes the GraphQL endpoint, the static client assets (the webpack bundle, css,
    fonts, graphics), the kill command, and the application page. The dataset-specific
    handlers from qed (preview/data/profile) are intentionally omitted; configuration,
    monitor, and launch traffic ride GraphQL queries/mutations/subscriptions added in later
    phases (see notes/gui-design.md section 4).
    """

    def dispatch(self, plexus, server, request):
        """Analyze the {request} and invoke the appropriate handler."""
        # get the request type and uri
        command = request.command
        url = request.url

        # show me the {url}
        journal.debug("pylith.ux.dispatch.url").log(f"{command}: {url}")

        # take a look
        match = self.regex.match(url)
        # if there is no match, we have a bug
        if not match:
            channel = journal.firewall("pylith.ux.dispatch")
            channel.line("could not find handler")
            channel.line(f"while resolving {url}")
            channel.log()
            return server.responses.NotFound(server=server)

        # find who matched and look up the handler
        token = match.lastgroup
        handler = getattr(self, token)
        # invoke it
        return handler(plexus=plexus, server=server, request=request, match=match)

    def __init__(self, plexus, docroot, pfs, **kwds):
        super().__init__(**kwds)
        # save the location of my document root so i can serve static assets
        self.docroot = docroot.discover()
        # attach it to the app's private filesystem
        pfs["ux"] = docroot
        # instantiate the {GraphQL} handler
        self.gql = GraphQL(plexus=plexus, dispatcher=self)

    # handlers
    def graphql(self, **kwds):
        """Handle a {graphql} request."""
        return self.gql.respond(**kwds)

    def stop(self, plexus, server, **kwds):
        """The client is asking me to die."""
        plexus.info.log("shutting down")
        return server.documents.Exit(server=server, code=128 + signal.SIGQUIT)

    def document(self, plexus, server, request, **kwds):
        """The client requested a document from the {plexus} pfs."""
        uri = "/ux" + request.url
        return server.documents.File(uri=uri, server=server, application=plexus)

    def css(self, plexus, server, request, **kwds):
        """The client requested a stylesheet."""
        uri = "/ux" + request.url
        return server.documents.CSS(uri=uri, server=server, application=plexus)

    def jscript(self, plexus, server, request, **kwds):
        """The client requested a script."""
        uri = "/ux" + request.url
        return server.documents.Javascript(uri=uri, server=server, application=plexus)

    def favicon(self, plexus, server, request, **kwds):
        """The client requested the app icon."""
        return server.responses.NotFound(server=server)

    def root(self, plexus, server, request, **kwds):
        """The client requested the root document."""
        uri = "/ux/{0.pyre_namespace}.html".format(plexus)
        return server.documents.File(uri=uri, server=server, application=plexus)

    # the app api
    regex = re.compile(
        "|".join(
            [
                # graphql requests
                r"/(?P<graphql>graphql)",
                # the kill command
                r"/(?P<stop>stop)",
                # document requests
                r"/(?P<css>.+\.css)",
                r"/(?P<jscript>.+\.js)",
                r"/(?P<document>(graphics/.+)|(fonts/.+)|(figures/.+))",
                r"/(?P<favicon>favicon.ico)",
                # everything else gets the app page; see the {root} resolver above
                r"/(?P<root>.*)",
            ]
        )
    )
