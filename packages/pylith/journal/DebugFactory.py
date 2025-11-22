# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import journal


class DebugFactory:

    @classmethod
    def application_flow(cls):
        return journal.debug("application-flow")

    @classmethod
    def auxiliary_fields(cls):
        return journal.debug("auxiliary-fields")

    @classmethod
    def integration_kernels(cls):
        return journal.debug("integration-kernels")

    @classmethod
    def mesh(cls):
        return journal.debug("mesh")

    @classmethod
    def mms_test(cls):
        return journal.debug("mms-test")

    @classmethod
    def solver(cls):
        return journal.debug("solver")

    @classmethod
    def todo(cls):
        return journal.debug("TODO")
