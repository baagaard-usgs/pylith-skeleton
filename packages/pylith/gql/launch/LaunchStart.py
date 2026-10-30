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
from .LaunchStartInput import LaunchStartInput
from .launcher import launcher


class LaunchStart(graphene.Mutation):
    """Start a local run.

    The run is the local equivalent of {pylith run}; the returned job is RUNNING. A start
    requested while a job is already running is refused by the launcher, and the GraphQL
    handler turns the refusal into an error document the client surfaces.
    """

    # the request payload
    class Arguments:
        input = LaunchStartInput(required=True)

    # the result is the job that was started
    job = graphene.Field(Job)

    @staticmethod
    def mutate(root, info, input):
        """Start a run with the given {input.target} and return the RUNNING job."""
        # reach the launcher the server owns
        backend = launcher(info)
        # if there is none, the server has not installed one; nothing can run
        if backend is None:
            # complain; the GraphQL handler turns this into an error document
            raise ValueError("the launcher is not available")
        # start the run; a double start raises, which becomes an error document
        job = backend.start()
        # resolve the mutation with the job as its source
        return LaunchStart(job=job)


# End of file
