# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import pathlib

import pylith

from ..protocols import data_writer


class DataWriterBase(pylith.component, implements=data_writer):
    """Base class for data writers."""

    @staticmethod
    def makeFilename(outputDir, simName, label, suffix):
        """Create filename from output directory, simulation name, label, and filename suffix."""
        return pathlib.Path(outputDir) / f"{simName}-{label}.{suffix}"

    @staticmethod
    def makePath(filename):
        """Create path for output file."""
        from ..mpi.Communicator import mpi_is_root

        isRoot = mpi_is_root()
        if isRoot:
            filePath = pathlib.Path(filename).parent.resolve()
            filePath.mkdir(exist_ok=True, parents=True)
