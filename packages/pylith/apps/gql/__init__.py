# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================

import graphene

from .Query import Query


# build the schema
# P0 exposes a read-only {version} query; mutations and the configuration/monitor/launch
# types arrive in later phases (see notes/gui-design.md sections 4-8).
schema = graphene.Schema(
    query=Query,
)
