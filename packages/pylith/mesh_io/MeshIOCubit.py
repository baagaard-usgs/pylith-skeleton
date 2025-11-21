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

from .. import protocols


class MeshIOCubit(pylith.component, implements=protocols.mesh_io, family="pylith.mesh_io.cubit"):

    filename = pylith.properties.uri(default=None)
    filename.doc = "URI of mesh file."

    # coord_sys = geocoords.coord_sys(default=geocoords.cs_cart)
    # coord_sys.doc = "Coordinate system associated with mesh."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"filename = {self.filename}",
            )
        )
        info.log()
        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement MeshIOCubit.__init__(). Pass parameters to C++.",))
        todo.log()
