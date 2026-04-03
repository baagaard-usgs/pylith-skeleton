import pathlib

import pytest

import pylith
from pylith import governing_eqns


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_elasticity.yaml")


def test_traits_defaults():
    eqn = governing_eqns.elasticity()  # Actor
    assert eqn().__class__.__name__ == "ElasticityEqn"
    assert eqn().materials
    assert eqn().interior_interfaces


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    eqn = test_subject.governing_eqn
    assert eqn.__class__.__name__ == "ElasticityEqn"
    assert len(eqn.materials) == 1
    assert eqn.materials[0].__class__.__name__ == "IsotropicLinear"
