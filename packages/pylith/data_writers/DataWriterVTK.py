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
from pylith import journal

from .DataWriter import DataWriterBase


class DataWriterVTK(DataWriterBase, family="pylith.data_writers.vtk"):
    """VTK data writer."""

    filename = pylith.properties.str()
    filename.doc = "Name of VTK file."

    time_format = pylith.properties.str(default="%f")
    time_format.doc = "C style format string for time stamp in filename."

    from pythia.pyre.units.time import second

    time_scale = pylith.properties.dimensional(default=1.0 * second, validator=pylith.properties.greater(0.0 * second))
    time_scale.doc = "Values used to normalize time stamp in filename."

    float_precision = pylith.properties.int(default=6, validator=pylith.properties.greater(0))
    float_precision.doc = "Precision of floating point values in output."

    def __init__(self):
        super().__init__(self)

        todo = journal.debug(":TODO:")
        todo.log("Implement DataWriterVTK time_history attribute. Requires spatialdata.")
        todo.log("Implement DataWriterVTK.__init__(). Pass parameters to C++.")

    def setFilename(self, outputDir, simName, label):
        """Set filename from default options and inventory. If filename is given in inventory, use it,
        otherwise create filename from default options.
        """
        filename = self.filename or DataWriterBase.makeFilename(outputDir, simName, label, "vtk")
        DataWriterBase.makePath(filename)

        todo = journal.debug(":TODO:")
        todo.log("Implement DataWriterHDF5.setFilename(). Pass parameters to C++.")
