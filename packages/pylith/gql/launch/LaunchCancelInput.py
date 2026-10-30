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


class LaunchCancelInput(graphene.InputObjectType):
    """The payload for cancelling a run.

    The {id} names the running job to stop; it is the identity the {job} query and the start
    mutation report.
    """

    # the running job to stop
    id = graphene.ID(required=True)


# End of file
