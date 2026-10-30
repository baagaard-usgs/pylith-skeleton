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


class LaunchTarget(graphene.Enum):
    """Where a simulation runs.

    Only {LOCAL} is accepted in this phase, where the run is a child of the web server.
    {REMOTE}, for a SLURM-over-SSH submission, is added with that backend; the panel reserves
    the selector for it now but leaves it disabled.
    """

    # run as a child of the web server
    LOCAL = "LOCAL"


# End of file
