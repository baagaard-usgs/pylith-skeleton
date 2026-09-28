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
def serial(**kwds):
    from .InitializerSerial import InitializerSerial
    __doc__ = InitializerSerial.__doc__
    if kwds:
        return InitializerSerial(**kwds)
    return InitializerSerial


@pylith.foundry(tip="Parallel initializer")
def parallel(**kwds):
    from .InitializerParallel import InitializerParallel
    __doc__ = InitializerParallel.__doc__
    if kwds:
        return InitializerParallel(**kwds)
    return InitializerParallel


@pylith.foundry(tip="Convert initializer")
def convert(**kwds):
    from .InitializerConvert import InitializerConvert
    __doc__ = InitializerConvert.__doc__
    if kwds:
        return InitializerConvert(**kwds)
    return InitializerConvert
