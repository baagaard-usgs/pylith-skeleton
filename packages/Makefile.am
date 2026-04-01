# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information. 
# =================================================================================================
SUBDIRS = \
	spatialdata \
	pylith

if ENABLE_CUBIT
make-manifest:
else
make-manifest:
	echo "exclude pylith/meshio/MeshIOCubit.py" > $@
endif

install-exec-local: make-manifest
	$(PYTHON) -m pip install --no-build-isolation $(top_srcdir)
