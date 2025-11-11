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


class DataWriterHDF5(DataWriterBase, family="pylith.data_writers.hdf5"):
    """VTK data writer."""

    filename = pylith.properties.str()
    filename.doc = "Name of VTK file."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.debug(":TODO:")
        todo.log("Implement DataWriterHDF5 time_history attribute. Requires spatialdata.")
        todo.log("Implement DataWriterHDF5.__init__(). Pass parameters to C++.")

    def setFilename(self, outputDir, simName, label):
        """Set filename from default options and inventory. If filename is given in inventory, use it,
        otherwise create filename from default options.
        """
        filename = self.filename or DataWriterBase.makeFilename(outputDir, simName, label, "h5")
        DataWriterBase.makePath(filename)

        todo = journal.debug(":TODO:")
        todo.log(
            (
                f"{self}",
                "Implement DataWriterHDF5.setFilename(). Pass parameters to C++.",
            )
        )
