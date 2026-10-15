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
from pylith.protocols import meshing


@pytest.fixture
def local_test_subject():
    yield LocalTestSubject
    pylith.reset()


class LocalTestSubject(pylith.component):

    refiner = meshing.refiner()


# End of file
