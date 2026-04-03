import pathlib

import pytest

import pylith
from pylith import problems


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_greens_fns.yaml")


def test_traits_defaults():
    problem = problems.greens_fns()  # Actor
    assert problem().__class__ == problems.GreensFns.GreensFns


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    problem = test_subject.problem
    assert problem.__class__ == problems.GreensFns.GreensFns
