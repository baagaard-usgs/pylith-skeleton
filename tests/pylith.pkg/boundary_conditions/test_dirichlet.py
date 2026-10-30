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
from pylith import boundary_conditions


@pytest.fixture
def load_yaml():
    cur_path = pyre.primitives.path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_dirichlet.yaml")


def test_traits_defaults():
    actor = boundary_conditions.dirichlet()
    bc = actor()  # Component instance
    assert bc.__class__ == boundary_conditions.Dirichlet.Dirichlet
    assert bc.field == "displacement"
    assert bc.label_name is None
    assert bc.label_value == 1
    assert bc.constrained_dof == ["x", "y", "z"]


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    bc = test_subject.bc  # Component instance
    assert bc.__class__ == boundary_conditions.Dirichlet.Dirichlet
    assert bc.field == "velocity"
    assert bc.label_name == "boundary_north"
    assert bc.label_value == 2
    assert bc.constrained_dof == ["x", "y"]


# End of file
