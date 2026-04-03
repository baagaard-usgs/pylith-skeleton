import pathlib

import pytest

import pylith
from pylith import initial_conditions


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_patch.yaml")


def test_traits_defaults():
    ic = initial_conditions.patch()  # Actor
    assert ic().__class__.__name__ == "InitialConditionPatch"
    assert ic.subfields == ["displacement"]
    assert ic.label_name is None
    assert ic.label_value == 1


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    ic = test_subject.ic
    assert ic.__class__.__name__ == "InitialConditionPatch"
    assert ic.subfields == ["velocity", "fluid_pressure"]
    assert ic.label_name == "test_patch"
    assert ic.label_value == 2
