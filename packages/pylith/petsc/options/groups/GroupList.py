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

from ....protocols.petsc.options import group


class GroupList(pylith.component, implements=group, family="pylith.petsc.options.group_list"):
    """PETSc options manager."""

    enabled = pylith.properties.bool(default=False)
    enabled.doc = "Use group of options if True."

    options = pylith.properties.list(schema=pylith.properties.tuple(schema=pylith.properties.str()))
    options.doc = "List of PETSc options as tuples."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"enabled = {self.enabled}",
                f"options = {self.options}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement GroupList.__init__(). Pass parameters to C++.",))
        todo.log()
