# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================

from pyre import PyreError


# the base class for my exceptions
class PyLithError(PyreError):
    """
    Base class for all pylith errors
    """


class ConfigurationError(PyLithError):

    def __init__(self, msg: str, component: str):
        super().__init__(self)
        self.msg = list(msg)
        self.component = component

    def __str__(self):
        header = [
            "Configuration Error:",
            str(self.component),
        ]
        return "\n".join(header + self.msg)
