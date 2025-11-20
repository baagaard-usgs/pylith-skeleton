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

from .MeshIO import MeshIO


class MeshIOAscii(pylith.component, implements=MeshIO, family="pylith.mesh_io.ascii"):

    filename = pylith.properties.uri(default=None)
    filename.doc = "URI of mesh file."

    # coord_sys = geocoords.coord_sys(default=geocoords.cs_cart)
    # coord_sys.doc = "Coordinate system associated with mesh."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement MeshIOAscii.__init__(). Pass parameters to C++.",
                f"filename={self.filename}",
            )
        )
        todo.log()
