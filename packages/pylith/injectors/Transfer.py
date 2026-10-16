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
# class Injector(pyre.component, family="pylith.injectors.material"):
#    """Inject value into material state."""
#
#    target = Material()
#    target.doc = "Material to inject value into."
#
#    value = pyre.properties.float(default=2.0)
#    value.doc = "Value to inject."
#
#    @pyre.export
#    def setState(self):
#        """Update state."""
#        self.target.setState(self.value)


# class Transfer(
#    pyre.component, family="pylith.transfer.material", implements=(Observer, Injector)
# ):
#    """Transfer state from one object to another."""
#
#    target = Material()
#    target.doc = "Material to inject value into."
#
#    def __init__(self, **kwds):
#        """Constructor."""
#        super().__init__(**kwds)
#        self.t = None
#
#    @pyre.export
#    def update(self, t):
#        """Update observer."""
#        self.t = t
#        self.setState()
#
#    @pyre.export
#    def setState(self):
#        """Update state."""
#        self.target.setState(self.t)


# End of file
