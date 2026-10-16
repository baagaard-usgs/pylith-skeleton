# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2026 All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================

from pyre import PyreError


# the base class for my exceptions
class SpatialDataError(PyreError):
    """
    Base class for all spatialdata errors
    """


# End of file
