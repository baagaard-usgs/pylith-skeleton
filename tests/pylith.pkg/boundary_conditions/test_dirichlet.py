import pathlib

import pytest

import pylith
from pylith import boundary_conditions


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_dirichlet.yaml")


def test_traits_defaults():
    bc = boundary_conditions.dirichlet() # Actor
    assert bc().__class__ == boundary_conditions.Dirichlet.Dirichlet
    assert bc.field == "displacement"
    assert bc.label_name == None
    assert bc.label_value == 1
    assert bc.constrained_dof == ["x", "y", "z"]


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    bc = test_subject.bc
    assert bc.__class__ == boundary_conditions.Dirichlet.Dirichlet
    assert bc.field == "velocity"
    assert bc.label_name == "boundary_north"
    assert bc.label_value == 2
    assert bc.constrained_dof == ["x", "y"]
