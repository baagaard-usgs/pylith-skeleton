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


@pylith.foundry(tip="Fault cohesive kinematic")
def fault_cohesive_kinematic():
    try:
        from .FaultCohesiveKinematic import FaultCohesiveKinematic
    except ImportError:
        return
    __doc__ = FaultCohesiveKinematic.__doc__
    return FaultCohesiveKinematic


@pylith.foundry(tip="Fault cohesive impulses")
def fault_cohesive_impulses():
    try:
        from .FaultCohesiveImpulses import FaultCohesiveImpulses
    except ImportError:
        return
    __doc__ = FaultCohesiveImpulses.__doc__
    return FaultCohesiveImpulses
