import pathlib

import pytest

from pyre.units.time import second

import pylith
from pylith import problems


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_time_dependent.yaml")


def test_traits_defaults():
    problem = problems.time_dependent()  # Actor
    assert problem().__class__ == problems.TimeDependent.TimeDependent
    assert problem.start_time == 0.0 * second
    assert problem.end_time == 0.0 * second
    assert problem.initial_time_step == 1.0 * second
    assert problem.max_time_steps == 20000


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    problem = test_subject.problem
    assert problem.__class__ == problems.TimeDependent.TimeDependent
    assert problem.start_time == 1.0 * second
    assert problem.end_time == 10.0 * second
    assert problem.initial_time_step == 0.5 * second
    assert problem.max_time_steps == 1000
