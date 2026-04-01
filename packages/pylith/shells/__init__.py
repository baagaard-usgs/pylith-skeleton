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


@pylith.foundry(tip="Action shell")
def action():
    try:
        from .Action import Action
    except ImportError:
        return
    __doc__ = Action.__doc__
    return Action


@pylith.foundry(tip="Command shell")
def command():
    try:
        from .Command import Command
    except ImportError:
        return
    __doc__ = Command.__doc__
    return Command


@pylith.foundry(tip="PyLith shell")
def pylith():
    try:
        from .Plexus import Plexus
    except ImportError:
        return
    __doc__ = Plexus.__doc__
    return Plexus
