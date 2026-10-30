# -*- Python -*-
# -*- coding: utf-8 -*-
#
# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2026, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================

import graphene

from .LaunchTarget import LaunchTarget


class LaunchStartInput(graphene.InputObjectType):
    """The payload for starting a run.

    The {target} says where the run goes; it defaults to {LOCAL}, the only value this phase
    accepts.
    """

    # where the run goes
    target = LaunchTarget(required=True, default_value=LaunchTarget.LOCAL)


# End of file
