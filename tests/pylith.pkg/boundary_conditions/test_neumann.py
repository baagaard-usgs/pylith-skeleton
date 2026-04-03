import pathlib

import pytest

import pylith
from pylith import boundary_conditions


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_neumann.yaml")


def test_traits_defaults():
    bc = boundary_conditions.neumann()  # Actor
    assert bc().__class__ == boundary_conditions.Neumann.Neumann
    assert bc.field == "displacement"
    assert bc.label_name is None
    assert bc.label_value == 1
    assert bc.scale_name == "stress"
    assert bc.ref_dir_1 == [0.0, 0.0, 1.0]
    assert bc.ref_dir_2 == [0.0, 1.0, 0.0]


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    bc = test_subject.bc
    assert bc.__class__ == boundary_conditions.Neumann.Neumann
    assert bc.field == "velocity"
    assert bc.label_name == "boundary_south"
    assert bc.label_value == 3
    assert bc.scale_name == "displacement"
    assert bc.ref_dir_1 == [1.0, 0.0, 0.0]
    assert bc.ref_dir_2 == [0.0, 0.0, 1.0]
