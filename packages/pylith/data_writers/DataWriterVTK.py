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
from pyre.units.time import second


import pylith

from .DataWriterBase import DataWriterBase


class DataWriterVTK(DataWriterBase, family="pylith.data_writers.vtk"):
    """VTK data writer."""

    filename = pylith.properties.uri()
    filename.doc = "Name of VTK file."

    time_format = pylith.properties.str(default="%f")
    time_format.doc = "C style format string for time stamp in filename."

    time_scale = pylith.properties.dimensional(default=1.0 * second)
    time_scale.validators = pyre.constraints.isGreater(value=0.0 * second)
    time_scale.doc = "Values used to normalize time stamp in filename."

    float_precision = pylith.properties.int(default=6)
    float_prevision = pyre.constraints.isPositive()
    float_precision.doc = "Precision of floating point values in output."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.debug_factory.todo()
        todo.report(
            (
                "Implement DataWriterVTK time_history attribute. Requires spatialdata.",
                "Implement DataWriterVTK.__init__(). Pass parameters to C++.",
            )
        )
        todo.log()

    def setFilename(self, outputDir, simName, label):
        """Set filename from default options and inventory. If filename is given in inventory, use it,
        otherwise create filename from default options.
        """
        filename = self.filename or DataWriterBase.makeFilename(outputDir, simName, label, "vtk")
        DataWriterBase.makePath(filename)

        todo = pylith.journal.debug_factory.todo()
        todo.log(("Implement DataWriterHDF5.setFilename(). Pass parameters to C++.",))
