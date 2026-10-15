# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2026 All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import journal


class ErrorFactory:

    @classmethod
    def configuration_error(cls):
        return journal.error("configuration-error")

    @classmethod
    def input_error(cls):
        return journal.error("input-error")

    @classmethod
    def external_error(cls):
        return journal.error("external-error")


# End of file
