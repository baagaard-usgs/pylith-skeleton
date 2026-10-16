# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2026 All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================

import pytest

import pylith.journal


@pytest.fixture
def factory():
    yield pylith.journal.warning_factory()


def test_user_input(factory):
    user_input = factory.user_input()
    assert user_input.name == "user-input"
    assert user_input.severity == "warning"


def test_deprecation(factory):
    deprecation = factory.deprecation()
    assert deprecation.name == "deprecation"
    assert deprecation.severity == "warning"


# End of file
