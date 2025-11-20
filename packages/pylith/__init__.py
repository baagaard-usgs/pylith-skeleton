# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================

from pyre import (
    properties,
    protocol,
    component,
    # decorators
    export,
    foundry,
    provides,
    # manager of pyre runtime
    executive,
    # shells
    application,
    plexus,
)

import journal

package = executive.registerPackage(name="pylith", file=__file__)
home, prefix, defaults = package.layout()


from . import meta
from . import exceptions

from . import shells
from . import cli


def version():
    """Return the version."""
    return meta.version


def copyright():
    """Return the copyright."""
    return print(meta.header)


def license():
    """Return the license."""
    return print(meta.license)


def credits():
    """Return the acknowledgments."""
    return print(meta.acknowledgments)
