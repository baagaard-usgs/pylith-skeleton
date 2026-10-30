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

from .Job import Job
from .LaunchCancelInput import LaunchCancelInput
from .launcher import launcher


class LaunchCancel(graphene.Mutation):
    """Cancel the running job.

    The launcher stops the job named {input.id}; the returned job is CANCELLED, or, if it had
    already finished when the request arrived, its terminal state. A request for a job that is
    not the one running returns the current record unchanged.
    """

    # the request payload
    class Arguments:
        input = LaunchCancelInput(required=True)

    # the result is the job that was cancelled
    job = graphene.Field(Job)

    @staticmethod
    def mutate(root, info, input):
        """Cancel the job named {input.id} and return its record."""
        # reach the launcher the server owns
        backend = launcher(info)
        # if there is none, the server has not installed one; nothing can be cancelled
        if backend is None:
            # complain; the GraphQL handler turns this into an error document
            raise ValueError("the launcher is not available")
        # cancel the job and resolve the mutation with its record as the source
        return LaunchCancel(job=backend.cancel(id=input.id))


# End of file
