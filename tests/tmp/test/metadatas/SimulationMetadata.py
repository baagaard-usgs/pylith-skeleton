# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pyre).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import pyre
import journal

from .Metadata import Metadata


class SimulationMetadata(pyre.component, implements=Metadata, family="test.metadatas.simulation_metadata"):
    """Metadata for simulation."""

    description = pyre.properties.str()
    description.doc = "Description of this simulation."

    authors = pyre.properties.list(schema=pyre.properties.str())
    authors.doc = "Creator(s) of this simulation."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        todo = journal.warning(":TODO:")
        todo.report(
            (
                f"{self}",
                "Implement SimulationMetadata.__init__(). Pass parameters to C++.",
                f"description={self.description}",
                f"authors={self.authors}",
            )
        )
        todo.log()
