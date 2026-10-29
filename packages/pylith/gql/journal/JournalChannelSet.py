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

import journal

from .JournalChannelSetInput import JournalChannelSetInput
from .JournalChannel import JournalChannel


class JournalChannelSet(graphene.Mutation):
    """Set whether a journal channel speaks.

    The change applies to the server's own journal, so the records the channel produces from
    now on reach, or stop reaching, the clients watching the stream.
    """

    # the request payload
    class Arguments:
        input = JournalChannelSetInput(required=True)

    # the result is the affected channel
    channel = graphene.Field(JournalChannel)

    @staticmethod
    def mutate(root, info, input):
        """Set the {input.active} flag of the {input.severity} channel named {input.name}."""
        # the channel identity
        channel = (input.severity, input.name)
        # if the severity is not one the journal knows
        if input.severity not in journal.severities:
            # complain; the GraphQL handler turns this into an error document
            raise ValueError(f"unknown journal severity '{input.severity}'")
        # build the instruction and apply it to this process's journal
        control = journal.control(severity=input.severity, name=input.name, active=input.active)
        control.apply()
        # the request context, which carries the server that took the request
        context = info.context or {}
        # the server, if there is one
        server = context.get("server")
        # the device that publishes records to clients keeps a census of channels; if the
        # server installed one, make sure this channel is on the list from now on
        device = getattr(server, "journal", None)
        if device is not None:
            # add the channel
            device.channels.add(channel)
        # resolve the mutation with the affected channel as its source
        return JournalChannelSet(channel=channel)


# End of file
