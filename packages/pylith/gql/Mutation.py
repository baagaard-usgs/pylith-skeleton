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

from .journal import journalChannelSet
from .launch import launchStart, launchCancel


class Mutation(graphene.ObjectType):
    """The top level mutation."""

    # turn a journal channel on or off
    journal_channel_set = journalChannelSet.Field()
    # start a local run
    launch_start = launchStart.Field()
    # cancel the running job
    launch_cancel = launchCancel.Field()


# End of file
