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
import pylith


@pylith.foundry(tip="PyLith application")
def pylith_app(**kwds):
    from .PyLithApp import PyLithApp

    __doc__ = PyLithApp.__doc__
    if kwds:
        return PyLithApp(**kwds)
    return PyLithApp


# End of file
