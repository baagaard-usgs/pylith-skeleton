import pathlib

import pytest

import pylith
from pylith import observers


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_solution_domain.yaml")


def test_traits_defaults():
    observer = observers.solution_domain()  # Actor
    assert observer().__class__ == observers.OutputSolnDomain.OutputSolnDomain
    assert observer.output_basis_order == 1
    assert observer.refine_levels == 0


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    observer = test_subject.observer
    assert observer.__class__ == observers.OutputSolnDomain.OutputSolnDomain
    assert observer.output_basis_order == 0
    assert observer.refine_levels == 1
