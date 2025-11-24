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

from .InitialConditionBase import InitialConditionBase


class InitialConditionDomain(InitialConditionBase, family="pylith.initial_conditions.domain"):
    """Initial condition over the domain."""

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report((f"{self}",))
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement InitialConditionDomain.__init__(). Pass parameters to C++.",))
        todo.log()
