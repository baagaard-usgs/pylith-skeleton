# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
from .Options import Options as options
from .OptionsManager import OptionsManager as options_manager

from . import groups


def options_class(name: str, sections: tuple):
    attributes = {
        "family": f"pylith.petsc.options.{name}",
    }
    for section in sections:
        attributes[section] = groups.group(default=groups.group_list)
    return type(name, (options_manager,), attributes)


default_sections = options_class("default_sections", sections=("testing", "collective_io", "attach_debugger"))
solver_sections = options_class(
    "solver_sections", sections=("solver", "initial_guess", "tolerances", "adaptive_ts", "monitoring")
)
