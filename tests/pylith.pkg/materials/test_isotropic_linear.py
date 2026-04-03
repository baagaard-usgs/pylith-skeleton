import pathlib

import pytest

import pylith
from pylith import governing_eqns


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_isotropic_linear.yaml")


def test_traits_defaults():
    material = governing_eqns.elasticity_eqn.bulk_rheologies.isotropic_linear()  # Actor
    assert material().__class__.__name__ == "IsotropicLinear"
    assert material.auxiliary_subfields
    assert material.derived_subfields


def test_traits_yaml(load_yaml):
    material = governing_eqns.elasticity_eqn.bulk_rheologies.isotropic_linear()  # Actor
    assert material.__class__.__name__ == "IsotropicLinear"
    # just loading config verifies no exceptions, subfield defaults still exist
    assert material.auxiliary_subfields
    assert material.derived_subfields
