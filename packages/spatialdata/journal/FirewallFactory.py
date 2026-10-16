# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2026 All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import journal


class FirewallFactory:

    @classmethod
    def internal_error(cls):
        return journal.firewall("internal-error")

    @classmethod
    def logic_error(cls):
        return journal.info("logic-error")


# End of file
