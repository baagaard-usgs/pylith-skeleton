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


@pylith.foundry(tip="Progress monitor time")
def progress_monitor_time(**kwds):
    from .ProgressMonitorTime import ProgressMonitorTime
    __doc__ = ProgressMonitorTime.__doc__
    if kwds:
        return ProgressMonitorTime(**kwds)
    return ProgressMonitorTime


@pylith.foundry(tip="Progress monitor step")
def progress_monitor_step(**kwds):
    from .ProgressMonitorStep import ProgressMonitorStep
    __doc__ = ProgressMonitorStep.__doc__
    if kwds:
        return ProgressMonitorStep(**kwds)
    return ProgressMonitorStep
