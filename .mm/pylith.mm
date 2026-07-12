# -*- Makefile -*-
#
# pylith project manifest


# the project assets
pylith.packages := pylith.pkg spatialdata.pkg

# a web bundle
pylith.webpack := pylith.web

pylith.tests := pylith.pytest spatialdata.pytest

# mpi is a Python runtime dependency (via mpi4py); declared here for documentation
pylith.extern := mpi

# load configurations
include $(pylith.packages)
include $(pylith.webpack)
include $(pylith.tests)


# end of file
