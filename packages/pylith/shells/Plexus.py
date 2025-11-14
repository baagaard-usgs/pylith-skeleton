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

from ..metadata import metadata as app_metadata
from ..defaults import defaults as sim_defaults
from ..problems import problem as app_problem
from ..petsc import options
from .. import journal as pylith_journal


class Plexus(pyre.plexus, family="pylith.shells.plexus"):
    """The main action dispatcher."""

    from .Action import Action as pyre_action

    metadata = app_metadata()
    metadata.doc = "Application metadata."

    defaults = sim_defaults()
    defaults.doc = "Simulation defaults."

    petsc_options = options.options(default=options.default_sections)
    petsc_options.doc = "General PETSc options."

    problem = app_problem()
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

        todo = pylith_journal.warning(":TODO:")
        todo.report(("Implement Plexus.__init__(). Pass parameters to C++.",))
        todo.log()

        self.metadata
        self.defaults
        self.petsc_options
        self.problem

    def run_cxx(self):
        flow = pylith_journal.info("application-flow", detail=0)
        flow.log("Running PyLith C++ application.")

        todo = pylith_journal.warning(":TODO:")
        todo.log("Call C++ PyLithApp::run().")
