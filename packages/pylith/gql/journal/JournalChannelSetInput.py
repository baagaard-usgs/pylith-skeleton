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


class JournalChannelSetInput(graphene.InputObjectType):
    """The payload for setting whether a journal channel speaks."""

    # the severity of the channel
    severity = graphene.String(required=True)
    # its name
    name = graphene.String(required=True)
    # whether it should speak
    active = graphene.Boolean(required=True)


# End of file
