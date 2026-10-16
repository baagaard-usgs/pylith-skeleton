# -*- Python -*-
# -*- coding: utf-8 -*-
# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2026 All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import pyre


class Observer(pyre.protocol, family="pylith.observers"):
    """Protocol declarator for observers."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {Observer} implementation"""
        return ObserverSolution

    @pyre.provides
    def update(self, t):
        """Update observer."""


class Injector(pyre.protocol, family="pylith.injectors"):
    """Protocol declarator for injectors."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {Injector} implementation"""
        return InjectValue

    @pyre.provides
    def setState(self):
        """Update state."""


class ObserveSolution(pyre.component, family="pylith.observers.solution"):
    """Observe solution."""

    @pyre.export
    def update(self, t):
        """Update observer."""
        print(f"Solution observer '{self.pyre_name}' t={t}.")


# End of file
