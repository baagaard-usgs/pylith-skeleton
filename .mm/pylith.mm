# -*- Makefile -*-
#
# pylith project manifest

#pylith.lib.c++.flags += $($(compiler.c++).std.c++23)

# the project assets
pylith.packages := pylith.pkg spatialdata.pkg

# web bundle
pylith.webpack := pylith.ux

# tests
pylith.tests := pylith.pytest spatialdata.pytest

# mpi is a Python runtime dependency (via mpi4py); declared here for documentation
pylith.extern := mpi

# load configurations
include $(pylith.packages)
include $(pylith.webpack)
include $(pylith.tests)


# end of file
