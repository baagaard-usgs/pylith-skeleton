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


def launcher(info):
    """Reach the launcher the server owns from the resolver {info}.

    The dispatcher exposes the launcher on the server in {install}, next to {server.journal};
    the GraphQL handler puts the server on {info.context}. A request that arrives before the
    server has installed the launcher, which should not happen in normal use, gets {None}, and
    the caller falls back to an idle view.
    """
    # the request context, which carries the server that took the request
    context = info.context or {}
    # the server, if there is one
    server = context.get("server")
    # the launcher it exposes, if it has installed one
    return getattr(server, "launcher", None)


# End of file
