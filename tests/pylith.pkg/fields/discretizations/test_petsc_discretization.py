import pathlib

import pytest

import pylith
from pylith.fields import discretizations


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_petsc_discretization.yaml")


def test_traits_defaults():
    actor = discretizations.petsc()
    discretization = actor()  # Component instance
    assert discretization.__class__ == discretizations.DiscretizationPetsc.DiscretizationPetsc
    assert discretization.basis_order is None
    assert discretization.quadrature_order is None
    assert discretization.dimension is None
    assert discretization.finite_element_space == "polynomial"
    assert discretization.cell_basis == "default"
    assert discretization.is_basis_continuous == True
    assert discretization.is_cohesive_only == False


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    discretization = test_subject.discretization
    assert discretization.__class__ == discretizations.DiscretizationPetsc.DiscretizationPetsc
    assert discretization.basis_order == 1
    assert discretization.quadrature_order == 2
    assert discretization.dimension == 3
    assert discretization.finite_element_space == "point"
    assert discretization.cell_basis == "tensor"
    assert discretization.is_basis_continuous == False
    assert discretization.is_cohesive_only == True
