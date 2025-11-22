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


class InfoFactory:

    @classmethod
    def about(cls):
        return journal.info("about")

    @classmethod
    def application_flow(cls, detail: int):
        channel = journal.info("application-flow")
        channel.detail = detail
        return channel

    @classmethod
    def application_flow_all(cls, detail: int):
        channel = journal.info("application-flow-all")
        channel.detail = detail
        return channel

    @classmethod
    def debug_config(cls):
        return journal.info("debug-config")

    @classmethod
    def initialization(cls, detail: int = 5):
        channel = journal.info("initialization")
        channel.detail = detail
        return channel
