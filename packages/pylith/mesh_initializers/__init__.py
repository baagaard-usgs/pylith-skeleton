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


@pylith.foundry(tip="Serial initializer")
def serial():
    try:
        from .InitializerSerial import InitializerSerial
    except ImportError:
        return
    __doc__ = InitializerSerial.__doc__
    return InitializerSerial


@pylith.foundry(tip="Parallel initializer")
def parallel():
    try:
        from .InitializerParallel import InitializerParallel
    except ImportError:
        return
    __doc__ = InitializerParallel.__doc__
    return InitializerParallel


@pylith.foundry(tip="Convert initializer")
def convert():
    try:
        from .InitializerConvert import InitializerConvert
    except ImportError:
        return
    __doc__ = InitializerConvert.__doc__
    return InitializerConvert
