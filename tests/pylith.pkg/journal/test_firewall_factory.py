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
    yield pylith.journal.firewall_factory()


def test_internal_error(factory):
    internal_error = factory.internal_error()
    assert internal_error.name == "internal-error"
    assert internal_error.severity == "firewall"


def test_logic_error(factory):
    logic_error = factory.logic_error()
    assert logic_error.name == "logic-error"
    assert logic_error.severity == "firewall"


# End of file
