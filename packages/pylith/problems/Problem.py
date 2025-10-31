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
from pylith import journal

from pylith import scales
from pylith import mesh_initializers


class Problem(pylith.protocol, family="pylith.problems"):
    """Boundary value problem to solve."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {Problem} implementation"""
        from .TimeDependent import TimeDependent

        return TimeDependent


class ProblemBase(pylith.component, implements=Problem):

    initialize_only = pylith.properties.bool(default=False)
    initialize_only.doc = "Initialize problem and then exit."

    scales = scales.scales(default=scales.quasistatic_elasticity)
    scales.doc = "Scales for nondimensionalizing problem."

    mesh_initializer = mesh_initializers.initializer(default=mesh_initializers.mesh_initializer)
    mesh_initializer.doc = "Initializer to read and setup finite-element mesh."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        self.scales
        self.mesh_initializer

        todo = journal.warning(":TODO:")
        todo.report(
            (
                "Implement Problem.__init__(). Pass parameters to C++.",
                f"initialize only={self.initialize_only}",
            )
        )
        todo.log()
