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

from ..protocols import application_defaults


class SimulationDefaults(pyre.component, implements=application_defaults, family="pylith.defaults.simulation_defaults"):
    """Default parameters for simulation."""

    output_dir = pylith.properties.str(default="output")
    output_dir.doc = "Directory for output."

    output_name = pylith.properties.str(default=None)
    output_name.doc = "Name for the problem (used with output_directory for default output filenames)."

    quadrature_order = pylith.properties.int(default=1)
    quadrature_order = pyre.constraints.isPositive()
    quadrature_order.doc = "Default quadrature order for finite-element integration."

    output_basis_order = pylith.properties.int(default=1)
    output_basis_order = pyre.constraints.isPositive()
    output_basis_order.doc = "Default basis order for output of fields."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement SimulationDefaults.__init__(). Pass parameters to C++.",
                f"output directory={self.output_dir}",
                f"output name={self.output_name}",
                f"quadrature order={self.quadrature_order}",
                f"output basis order={self.output_basis_order}",
            )
        )
        todo.log()
