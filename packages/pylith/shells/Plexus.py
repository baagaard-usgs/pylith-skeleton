# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import pyre
import journal

import pylith

from .. import protocols
from ..protocols import petsc
from ..petsc import options


class Plexus(pyre.plexus, family="pylith.shells.plexus"):
    """The main action dispatcher."""

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
        if self.log_file:
            # redirect all journal output to the file
            journal.logfile(name=str(self.log_file), mode="w")

        todo = pylith.journal.debug_factory.todo()
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
        flow = pylith.journal.info_factory.application_flow(detail=0)
        flow.log("Running PyLith C++ application.")

        todo = pylith.journal.debug_factory.todo()
        todo.log("Call C++ PyLithApp::run().")
