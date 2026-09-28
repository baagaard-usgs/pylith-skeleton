# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import pylith


@pylith.foundry(tip="Create cohesive cells")
def create_cohesive_cells(**kwds):
    from .CreateCohesiveCells import CreateCohesiveCells
    __doc__ = CreateCohesiveCells.__doc__
    if kwds:
        return CreateCohesiveCells(**kwds)
    return CreateCohesiveCells
