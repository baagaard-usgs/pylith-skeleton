# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2026 All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import journal


class DebugFactory:

    @classmethod
    def application_flow(cls):
        return journal.debug("application-flow")

    @classmethod
    def todo(cls):
        return journal.debug("TODO")


# End of file
