import pathlib

import pytest

import pylith
from pylith import initial_conditions


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_domain.yaml")


def test_traits_defaults():
    ic = initial_conditions.domain()  # Actor
    assert ic().__class__.__name__ == "InitialConditionDomain"
    assert ic.subfields == ["displacement"]


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    ic = test_subject.initial_condition
    assert ic.__class__.__name__ == "InitialConditionDomain"
    assert ic.subfields == ["displacement", "velocity"]
