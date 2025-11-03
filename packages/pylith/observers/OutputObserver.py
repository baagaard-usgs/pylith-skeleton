# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import pyre

import pylith
from pylith import journal
from pylith.observers import output_triggers
from pylith import data_writers

from .Observer import Observer


class OutputObserver(Observer):
    """Abstract base class for output observers."""

    trigger = output_triggers.output_trigger(default=output_triggers.step())
    trigger.doc = "Trigger defining how often output is written."

    writer = data_writers.data_writer(default=data_writers.hdf5())
    writer.doc = "Writer for data."

    output_basis_order = pylith.properties.int(default=1)
    output_basis_order.validators = pyre.constraints.isMember(0, 1)
    output_basis_order.doc = "Basis order for output."

    refine_levels = pylith.properties.int(default=0)
    refine_levels.validators = pyre.constraints.isGreaterEqual(value=0)
    refine_levels.doc = "Number of mesh refinement levels for output."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.warning(":TODO:")
        todo.report(
            (
                "Implement OutputObserver.__init__(). Pass parameters to C++.",
                f"trigger={self.trigger}",
                f"writer={self.writer}",
                f"output basis order={self.output_basis_order}",
                f"refine levels={self.refine_levels}",
            )
        )
        todo.log()
