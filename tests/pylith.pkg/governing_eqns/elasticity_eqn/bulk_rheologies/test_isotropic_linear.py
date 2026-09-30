import pathlib

import pytest

import pylith
from pylith.governing_eqns.elasticity_eqn import bulk_rheologies


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_isotropic_linear.yaml")


def test_traits_defaults():
    actor = bulk_rheologies.isotropic_linear()
    material = actor()  # Component instance
    assert material.__class__ == pylith.governing_eqns.elasticity_eqn.bulk_rheologies.IsotropicLinear.IsotropicLinear
    assert material.label_name is None
    assert material.label_value == 1
    assert material.observers == []
    assert material.auxiliary_subfields
    assert material.derived_subfields


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")  # Instantiated component
    material = test_subject.material
    assert material.__class__ == pylith.governing_eqns.elasticity_eqn.bulk_rheologies.IsotropicLinear.IsotropicLinear
    assert material.label_name == "material-id"
    assert material.label_value == 2
    assert material.observers == []
    assert material.auxiliary_subfields

    shear_modulus = material.auxiliary_subfields.shear_modulus
    assert shear_modulus.alias == "shear_modulus"
    bulk_modulus = material.auxiliary_subfields.bulk_modulus
    assert bulk_modulus.alias == "bulk_modulus"
    reference_stress = material.auxiliary_subfields.reference_stress
    assert reference_stress.enabled

    cauchy_stress = material.derived_subfields.cauchy_stress
    assert cauchy_stress.enabled
    cauchy_strain = material.derived_subfields.cauchy_strain
    assert cauchy_strain.enabled
