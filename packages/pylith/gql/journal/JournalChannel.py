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


class JournalChannel(graphene.ObjectType):
    """A journal channel the server offers, and whether it speaks.

    The channel is identified by its {severity} and {name}; the {active} and {fatal} state is
    read from the live journal on every request, so the answer is always current.
    """

    # my fields
    id = graphene.ID(required=True)
    severity = graphene.String(required=True)
    name = graphene.String(required=True)
    active = graphene.Boolean(required=True)
    fatal = graphene.Boolean(required=True)

    # the resolvers; the source is a {(severity, name)} pair
    @staticmethod
    def resolve_id(channel, info, **kwds):
        """Make an id out of the {channel} identity."""
        severity, name = channel
        return f"{severity}:{name}"

    @staticmethod
    def resolve_severity(channel, info, **kwds):
        """Report the severity of the {channel}."""
        return channel[0]

    @staticmethod
    def resolve_name(channel, info, **kwds):
        """Report the name of the {channel}."""
        return channel[1]

    @staticmethod
    def resolve_active(channel, info, **kwds):
        """Report whether the {channel} speaks."""
        return JournalChannel.live(channel=channel).active

    @staticmethod
    def resolve_fatal(channel, info, **kwds):
        """Report whether the {channel} aborts after speaking."""
        return JournalChannel.live(channel=channel).fatal

    # implementation details
    @staticmethod
    def live(channel):
        """Open the live journal channel that {channel} identifies."""
        severity, name = channel
        # find the factory for the severity
        factory = journal.severities[severity]
        # and open the channel; the state is shared by everybody with this name
        return factory(name)


# End of file
