# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
from journal import *


def info_factory():
    try:
        from .InfoFactory import InfoFactory
    except ImportError:
        return
    __doc__ = InfoFactory.__doc__
    return InfoFactory


def warning_factory():
    try:
        from .WarningFactory import WarningFactory
    except ImportError:
        return
    __doc__ = WarningFactory.__doc__
    return WarningFactory


def error_factory():
    try:
        from .ErrorFactory import ErrorFactory
    except ImportError:
        return
    __doc__ = ErrorFactory.__doc__
    return ErrorFactory


def firewall_factory():
    try:
        from .FirewallFactory import FirewallFactory
    except ImportError:
        return
    __doc__ = FirewallFactory.__doc__
    return FirewallFactory


def debug_factory():
    try:
        from .DebugFactory import DebugFactory
    except ImportError:
        return
    __doc__ = DebugFactory.__doc__
    return DebugFactory


