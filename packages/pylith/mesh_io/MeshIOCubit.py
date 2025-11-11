# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================

# from spatialdata.geocoords.CSCart import CSCart

import pylith
from pylith import journal
from pylith.utils import constraints

from .MeshIO import MeshIO


class MeshIOCubit(pylith.component, implements=MeshIO, family="pylith.mesh_io.cubit"):

    filename = pylith.properties.uri()
    filename.validators = constraints.notEmptyString()
    filename.doc = "URI of mesh file."

    # coord_sys = geocoords.coord_sys(default=geocoords.cs_cart)
    # coord_sys.doc = "Coordinate system associated with mesh."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement MeshIOCubit.__init__(). Pass parameters to C++.",
                f"filename={self.filename}",
            )
        )
        todo.log()
