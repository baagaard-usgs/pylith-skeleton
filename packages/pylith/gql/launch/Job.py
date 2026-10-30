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


class Job(graphene.ObjectType):
    """A launched simulation and the state it is in.

    The record is scheduler-agnostic, so the local launcher and a future SLURM backend
    present the same shape. The {state} is a plain string to match the schema's style, where
    the journal types carry severities as strings rather than enums. The {command},
    {startedAt}, and {exitCode} fields are null until they are known: all three while the job
    is IDLE, and {exitCode} while it runs and for a cancelled run.
    """

    # my fields
    id = graphene.ID(required=True)
    state = graphene.String(required=True)
    command = graphene.String()
    started_at = graphene.String()
    exit_code = graphene.Int()

    # the resolvers; the source is a {pylith.apps.launch.Job} record
    @staticmethod
    def resolve_id(job, info, **kwds):
        """Report the identity of the {job}."""
        return job.id

    @staticmethod
    def resolve_state(job, info, **kwds):
        """Report the state of the {job}."""
        return job.state

    @staticmethod
    def resolve_command(job, info, **kwds):
        """Report the command line the {job} ran, or nothing while idle."""
        return job.command

    @staticmethod
    def resolve_started_at(job, info, **kwds):
        """Report when the {job} started, or nothing while idle."""
        return job.started_at

    @staticmethod
    def resolve_exit_code(job, info, **kwds):
        """Report the exit code of the {job}, or nothing until it ends."""
        return job.exit_code


# End of file
