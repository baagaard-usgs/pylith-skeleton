# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2026 All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================

import pytest

import pyre

import pylith
from pylith import initial_conditions


@pytest.fixture
def load_yaml():
    cur_path = pyre.primitives.path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_domain.yaml")


def test_traits_defaults():
    actor = initial_conditions.domain()
    ic = actor()  # Component instance
    assert ic.__class__ == initial_conditions.InitialConditionDomain.InitialConditionDomain
    assert ic.subfields == ["displacement"]


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    ic = test_subject.ic
    assert ic.__class__ == initial_conditions.InitialConditionDomain.InitialConditionDomain
    assert ic.subfields == ["displacement", "velocity"]


# End of file
