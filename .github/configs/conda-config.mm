# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2026 All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
# External dependencies configuration file for mm with conda.
# Installed to ~/.mm
# 
# Based on the CI setup for Pyre.

# external dependencies
# system tools
sys.prefix := $(CONDA_PREFIX)

# mpi
mpi.executive := mpiexec
hdf5.parallel := no # Don't need to link against MPI

# End of file
