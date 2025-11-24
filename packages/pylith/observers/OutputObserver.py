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

from .. import protocols
from ..protocols import observers


class OutputObserver(pylith.component, implements=protocols.observer):
    """Abstract base class for output observers."""

    trigger = observers.output_trigger()
    trigger.doc = "Trigger defining how often output is written."

    writer = protocols.data_writer()
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

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"trigger = {self.trigger}",
                f"writer = {self.writer}",
                f"output basis order = {self.output_basis_order}",
                f"refine levels = {self.refine_levels}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement OutputObserver.__init__(). Pass parameters to C++.",))
        todo.log()
