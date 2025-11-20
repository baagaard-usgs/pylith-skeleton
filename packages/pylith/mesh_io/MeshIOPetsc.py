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


class MeshIOPetsc(pylith.component, implements=MeshIO, family="pylith.mesh_io.petsc"):

    filename = pylith.properties.uri(default=None)
    filename.doc = "URI of mesh file."

    gmsh_mark_recursive = pylith.properties.bool(default=False)
    gmsh_mark_recursive.doc = "Gmsh file marks faces, edges, and vertices rather than just faces (3D) or edges (2D)."

    petsc_options_prefix = pylith.properties.str(default="")
    petsc_options_prefix.doc = "PETSc options prefix for this mesh."

    # coord_sys = geocoords.coord_sys(default=geocoords.cs_cart)
    # coord_sys.doc = "Coordinate system associated with mesh."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = pylith.journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement MeshIOPetsc.__init__(). Pass parameters to C++.",
                f"filename={self.filename}",
                f"Gmsh mark recursive={self.gmsh_mark_recursive}",
                f"PETSc options prefix={self.petsc_options_prefix}",
            )
        )
        todo.log()
