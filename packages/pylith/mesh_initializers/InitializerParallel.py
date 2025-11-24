# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import pylith

from ..protocols import mesh_initializer
from ..protocols.mesh_initializers import initialize_phase

from . import phases


class InitializerParallel(pylith.component, implements=mesh_initializer, family="pylith.mesh_initializers.parallel"):

    reader = initialize_phase(default=phases.reader)
    reader.doc = "Read mesh."

    distributor = initialize_phase(default=phases.distributor)
    distributor.doc = "Distribute mesh."

    insert_interfaces = initialize_phase(default=phases.insert_interfaces)
    insert_interfaces.doc = "Insert interior interfaces."

    refiner = initialize_phase(default=phases.refiner)
    refiner.doc = "Refine mesh."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"reader = {self.reader}",
                f"distributor = {self.distributor}",
                f"insert interfaces = {self.insert_interfaces}",
                f"refiner = {self.refiner}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(
            "Implement InitializerParallel.__init__(). Pass parameters to C++.",
        )
        todo.log()
