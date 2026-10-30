# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2026 All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import os

import pyre
import journal

import pylith

from .. import protocols
from ..protocols import petsc
from ..petsc import options


class Plexus(pyre.plexus, family="pylith.shells.plexus"):
    """The main action dispatcher."""

    # Required by pyre.plexus
    from .Action import Action as pyre_action

    metadata = protocols.application_metadata()
    metadata.doc = "Application metadata."

    defaults = protocols.application_defaults()
    defaults.doc = "Simulation defaults."

    petsc_options = petsc.options_manager(default=options.simulation_options)
    petsc_options.doc = "General PETSc options."

    problem = protocols.problem()
    problem.doc = "Boundary value problem to solve."

    # journal control; useful until journal is once again configurable
    log_file = pylith.properties.path()
    log_file.default = None
    log_file.doc = "File that captures all journal output."

    def __init__(self, **kwds):
        super().__init__(**kwds)
        # the pyre application shell registers my nickname as the journal application name;
        # clear it so user-facing channels tag messages with the channel severity
        # ("info (application-flow)") rather than the nickname
        journal.application("")
        if self.log_file:
            # redirect all journal output to the file
            journal.logfile(name=str(self.log_file), mode="w")
        # when launched as a child of the web server, ship journal records to the parent in
        # their wire form, so the Monitor renders them as the native channels they are
        self._shipJournal()

        todo = pylith.journal.debug_factory().todo()
        todo.report(
            (
                f"{self}",
                "Implement Plexus.__init__(). Pass parameters to C++.",
                f"metadata = {self.metadata}",
                f"defaults = {self.defaults}",
                f"PETSc options = {self.petsc_options}",
                f"problem = {self.problem}",
            )
        )
        todo.log()

    def run_cxx(self):
        flow = pylith.journal.info_factory().application_flow(detail=0)
        flow.log("Running PyLith C++ application.")

        todo = pylith.journal.debug_factory().todo()
        todo.log("Call C++ PyLithApp::run().")

    # web shell support (launch with: pylith --shell=web --shell.auto=yes)
    def pyre_mountApplicationFolders(self, pfs, prefix, **kwds):
        """Explore the installation folders and locate the web document root."""
        # chain up
        pfs = super().pyre_mountApplicationFolders(pfs=pfs, prefix=prefix, **kwds)
        # get my namespace
        namespace = self.pyre_namespace

        # this is early times, so {prefix} may not be explored; proceed carefully.
        # the web client bundle is installed under {prefix}/etc/{namespace}/ux; the source
        # tree that produces it lives in the repo's web/ directory (see notes/gui-design.md
        # section 9).
        docroot = prefix
        for name in ["etc", namespace, "ux"]:
            # fill the contents of the current node
            docroot.discover(levels=1)
            try:
                # descend to the next level
                docroot = docroot[name]
            except prefix.NotFoundError:
                # complain and disable the web shell
                channel = self.warning
                channel.line("while looking for UX support:")
                channel.line(f"directory '{docroot.uri}/{name}' not found")
                channel.line("disabling the web shell")
                channel.log()
                self._ux = None
                break
        else:
            # import lazily so the {graphene} dependency is only required on the web path
            from ..apps import ux

            # instantiate and attach my dispatcher
            self._ux = ux.dispatcher(plexus=self, docroot=docroot, pfs=pfs)

        # all done
        return pfs

    def _shipJournal(self):
        """Send journal records to the parent process in their wire form, if asked.

        The web-server launcher runs me as a child and hands me a pipe to its event loop,
        naming the write descriptor in the {journalPipe} environment variable. When it is
        set, I make a courier on that descriptor my journal device, so my records reach the
        parent as structured records it can render as the native channels they are.

        The courier does not mirror to the console it replaces: the launcher reads my {stdout}
        to catch output that is not a journal record, and a console that rendered every record
        there as well would feed each one back as a second, {stdout} record. The pipe is the
        one path my journal takes to the parent.
        """
        # the descriptor the parent handed me, if any
        descriptor = os.environ.get(self.journalPipe)
        # if the parent did not ask for records, there is nothing to do
        if descriptor is None:
            # all done
            return
        # make a courier on the pipe my journal device; hold a reference of my own so it stays
        # alive for as long as i am producing records, rather than resting only on the
        # chronicler's device slot
        self._courier = journal.courier(descriptor=int(descriptor))
        journal.chronicler.device = self._courier
        # all done
        return

    def pyre_respond(self, server, request):
        """Fulfill an HTTP request."""
        # get my dispatcher
        ux = self._ux
        # if i don't have one, there is something wrong with my installation
        if ux is None:
            return server.responses.NotFound(server=server)
        # the stock Pyre web shell gives me no server until a request arrives; this is the
        # earliest the dispatcher can reach the server, so install the journal publishing
        # device now, before any client connects, rather than on the first stream subscription
        ux.install(server=server)
        # ask the dispatcher to do its thing
        return ux.dispatch(plexus=self, server=server, request=request)

    # constants
    # the environment variable that names the descriptor on which the web-server launcher
    # wants my journal records shipped in their wire form; shared with the launcher that
    # spawns me (see pylith.apps.launch.LocalLauncher)
    journalPipe = "PYLITH_JOURNAL_FD"

    # private data
    _ux = None  # the UX manager
    _courier = None  # the journal courier that ships my records to the launcher, if any


# End of file
