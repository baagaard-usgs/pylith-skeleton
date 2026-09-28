import pathlib

import pytest

import pylith
from pylith.governing_eqns.elasticity_eqn import solution_subfields


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_elasticity_solution_nofault.yaml")


def test_traits_defaults():
    actor = solution_subfields.no_fault()
    solution = actor()  # Component instance
    assert (
        solution.__class__ == pylith.governing_eqns.elasticity_eqn.solution_subfields.SubfieldsNoFault.SubfieldsNoFault
    )

    displacement = solution.displacement
    assert displacement.alias is None
    assert displacement.discretization.basis_order is None

    velocity = solution.velocity
    assert velocity.alias is None
    assert velocity.discretization.basis_order is None


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")  # Instantiated component
    solution = test_subject.solution
    assert (
        solution.__class__ == pylith.governing_eqns.elasticity_eqn.solution_subfields.SubfieldsNoFault.SubfieldsNoFault
    )

    displacement = solution.displacement
    assert displacement.alias == "displacement"
    assert displacement.discretization.basis_order == 2

    velocity = solution.velocity
    assert velocity.alias == "velocity"
    assert velocity.discretization.basis_order == 3
