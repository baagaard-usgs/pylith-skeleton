# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2026 All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================

import pytest

import pylith
from pylith.protocols import petsc


@pytest.fixture
def local_test_subject():
    yield LocalTestSubject
    pylith.reset()


class LocalTestSubject(pylith.component):

    options_manager = petsc.options_manager()


# End of file
