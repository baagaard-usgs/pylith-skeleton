import pathlib

import pytest

import pylith
from pylith import governing_eqns


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_elasticity.yaml")


def test_traits_defaults():
    actor = governing_eqns.elasticity()
    eqn = actor()  # Component instance
    assert eqn.__class__ == governing_eqns.Elasticity.Elasticity
    assert len(eqn.materials) == 1

    material = eqn.materials[0]()  # Component instance
    assert material.__class__ == pylith.governing_eqns.elasticity_eqn.bulk_rheologies.IsotropicLinear.IsotropicLinear


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    eqn = test_subject.governing_eqn
    assert eqn.__class__ == governing_eqns.Elasticity.Elasticity
    assert len(eqn.materials) == 2

    material = eqn.materials[0]
    assert material.pyre_name == "crust"
    assert material.__class__ == pylith.governing_eqns.elasticity_eqn.bulk_rheologies.IsotropicLinear.IsotropicLinear

    material = eqn.materials[1]
    assert material.pyre_name == "mantle"
    assert material.__class__ == pylith.governing_eqns.elasticity_eqn.bulk_rheologies.IsotropicLinear.IsotropicLinear
