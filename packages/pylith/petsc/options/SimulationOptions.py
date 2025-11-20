# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import pylith

from .ManagerBase import ManagerBase

from . import groups


class SimulationOptions(ManagerBase, family="pylith.petsc.options.simulation"):
    """PETSc options manager for simulation-level options."""

    testing = groups.group(default=groups.group_list)
    testing.doc = "Options to enable additional checks for use in testing."

    collective_io = groups.group(default=groups.group_list)
    collective_io.doc = "Turn on HDF5 collective I/O."

    attach_debugger = groups.group(default=groups.group_list)
    attach_debugger.doc = "Options to attach a debugger on simulation startup."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement SimulationOptions.__init__(). Pass parameters to C++.",
            )
        )
        todo.log()
