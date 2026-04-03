import pathlib

import pytest

import pylith
from pylith import observers


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_solution_boundary.yaml")


def test_traits_defaults():
    observer = observers.solution_boundary()  # Actor
    assert observer().__class__ == observers.OutputSolnBoundary.OutputSolnBoundary
    assert observer.output_basis_order == 1
    assert observer.refine_levels == 0
    assert observer.label_name is None
    assert observer.label_value == 1


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    observer = test_subject.observer
    assert observer.__class__ == observers.OutputSolnBoundary.OutputSolnBoundary
    assert observer.output_basis_order == 0
    assert observer.refine_levels == 2
    assert observer.label_name == "test_boundary"
    assert observer.label_value == 3
