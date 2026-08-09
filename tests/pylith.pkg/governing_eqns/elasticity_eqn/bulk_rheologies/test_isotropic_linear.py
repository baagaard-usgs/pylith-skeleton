import pathlib

import pytest

import pylith
from pylith.governing_eqns.elasticity import bulk_rheologies


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_isotropic_linear.yaml")


def test_traits_defaults():
    material = bulk_rheologies.isotropic_linear()  # Actor
    assert material().__class__ == pylith.governing_eqns.elasticity_eqn.bulk_rheologies.IsotropicLinear.IsotropicLinear
    assert material.auxiliary_subfields
    assert material.derived_subfields


def test_traits_yaml(load_yaml):
    material = bulk_rheologies.isotropic_linear()  # Actor
    assert material.__class__ == pylith.governing_eqns.elasticity_eqn.bulk_rheologies.IsotropicLinear.IsotropicLinear
    # just loading config verifies no exceptions, subfield defaults still exist
    assert material.auxiliary_subfields
    assert material.derived_subfields
