# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import pyre

import pylith

from ... import protocols
from ...protocols.mesh_initializers import distributor

# from pylith.data_writers import data_writer_hdf5


class DistributorPetsc(pylith.component, implements=distributor, family="pylith.mesh_initializers.distributor.petsc"):

    partitioner = pylith.properties.str(default="parmetis")
    partitioner.validators = pyre.constraints.isMember("parmetis", "chaco", "simple")
    partitioner.doc = "Name of mesh partitioner (PETSc must be built with support for requested partitioner)."

    use_edge_weighting = pylith.properties.bool(default=True)
    use_edge_weighting.doc = "Use edge weighting when partitioning mesh (parmetis only)."

    write_partition = pylith.properties.bool(default=False)
    write_partition.doc = "Write partition information to file."

    data_writer = protocols.data_writer()
    data_writer.doc = "Data writer for partition information."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"partitioner = {self.partitioner}",
                f"use edge weighting = {self.use_edge_weighting}",
                f"write_partition = {self.write_partition}",
                f"data writer = {self.data_writer}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement DistributorPetsc.__init__(). Pass parameters to C++.",))
        todo.log()
