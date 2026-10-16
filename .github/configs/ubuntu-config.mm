# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2026 All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
# External dependencies configuration file for mm on Linux.
# Installed to ~/.mm
# 
# Based on the CI setup for Pyre.

# external dependencies
# system tools
sys.prefix := /usr
sys.lib := $(sys.prefix)/lib/x86_64-linux-gnu

# gsl
gsl.version := 2.8
gsl.dir := $(sys.prefix)

# hdf5
hdf5.version := 1.14.6
hdf5.dir := $(sys.prefix)
hdf5.parallel := serial
hdf5.incpath := $(hdf5.dir)/include/hdf5/$(hdf5.parallel)
hdf5.libpath := $(sys.lib)/hdf5/$(hdf5.parallel)

# mpi
mpi.version := 5.0.10
mpi.flavor := openmpi
mpi.dir := $(sys.lib)/$(mpi.flavor)
mpi.executive := mpiexec

# python
python.version := $(pythonVersion)
python.dir := $(pythonLocation)

# pybind11
pybind11.version := 3.0.1
pybind11.dir := $(python.dir)/lib/python$(python.version)/site-packages/pybind11

# control over the build process
# the clang drivers
clang.driver := clang-$(suiteVersion)
clang++.driver := clang++-$(suiteVersion)
# the gcc drivers
gcc.driver := gcc-$(suiteVersion)
g++.driver := g++-$(suiteVersion)
# the python driver
python3.driver := python$(python.version)


# End of file
