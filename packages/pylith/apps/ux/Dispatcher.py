# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2026, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================

import re
import signal

import journal

from .GraphQL import GraphQL
from .Journal import Journal
from ..launch import LocalLauncher


class Dispatcher:
    """The handler of web requests.

    P0 routes the GraphQL endpoint, the static client assets (the webpack bundle, css,
    fonts, graphics), the stop command, and the application page. The dataset-specific
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
        # the journal device that publishes records to clients; installed on the chronicler the
        # first time the server is in reach (see {install})
        self.device = None
        # the launcher that runs simulations locally; built the first time the server is in
        # reach, since it needs the server's event loop (see {install})
        self.launcher = None

    # handlers
    def graphql(self, **kwds):
        """Handle a {graphql} request."""
        return self.gql.respond(**kwds)

    def journal(self, server, **kwds):
        """Open a server-sent event stream that carries journal records.

        The stream opens with the history the device has gathered, so a client that connects
        late still sees the records that came before it.
        """
        # the device is installed when the server first comes in reach; get it
        device = self.device
        # the history it holds, framed for a newcomer, or nothing if there is none
        opening = device.opening()
        # hand back a streaming response on the journal topic
        return server.eventStream(server=server, topic=device.topic, opening=opening)

    def stop(self, plexus, server, **kwds):
        """The client is asking me to stop."""
        plexus.info.log("shutting down")
        return server.documents.Exit(server=server, exitCode=128 + signal.SIGQUIT)

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

    # interface
    def install(self, server):
        """Install the journal publishing device and the launcher, once.

        Called the first time {server} is in reach, before any client connects, so the history
        begins at server contact rather than at the first stream subscription. The device
        mirrors every entry to the device that was writing before it, typically the terminal, so
        the records keep reaching the console. The launcher is built here too, since it needs
        the server's event loop and hub to run and watch the child process.
        """
        # if the device is already installed, so is the launcher; hand the device back
        if self.device is not None:
            # nothing more to do
            return self.device
        # the device the journal has been writing to, typically the terminal
        terminal = journal.chronicler.device
        # build my device, mirroring to the terminal
        self.device = Journal(server=server, mirror=terminal)
        # install it as the chronicler's device, so every entry reaches it
        journal.chronicler.device = self.device
        # the server exposes its device to the GraphQL layer, which adds a channel to the
        # census when a mutation turns one on
        server.journal = self.device
        # build the launcher, which runs simulations on the server's event loop
        self.launcher = LocalLauncher(server=server)
        # and expose it on the server, so the GraphQL layer reaches it the way it reaches the
        # journal device
        server.launcher = self.launcher
        # hand the device back
        return self.device

    # the app api
    regex = re.compile(
        "|".join(
            [
                # graphql requests
                r"/(?P<graphql>graphql)",
                # the journal event stream
                r"/(?P<journal>journal)",
                # the stop command
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
