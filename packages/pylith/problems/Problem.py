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

from ..scales import scales
from .. import mesh_initializers
from .. import governing_eqns


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

    scales = scales()
    scales.doc = "Scales for nondimensionalizing problem."

    mesh_initializer = mesh_initializers.initializer()
    mesh_initializer.doc = "Initializer to read and setup finite-element mesh."

    governing_eqn = governing_eqns.governing_eqn()
    governing_eqn.doc = "Governing equations for boundary value problem."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement Problem.__init__(). Pass parameters to C++.",
                f"initialize only={self.initialize_only}",
                f"scales={self.scales}",
                f"mesh initializer={self.mesh_initializer}",
                f"governing equation={self.governing_eqn}",
            )
        )
        todo.log()
