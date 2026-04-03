import pathlib

import pytest

import pylith
from pylith.interior_interfaces import source_time_fns


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_step.yaml")


def test_traits_defaults():
    source_fn = source_time_fns.step()  # Actor
    assert source_fn().__class__ == source_time_fns.Step.Step


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    source_fn = test_subject.source_fn
    assert source_fn.__class__ == source_time_fns.Step.Step
