import pathlib

import pytest

import pylith
from pylith.petsc.options import groups


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_group_list.yaml")


def test_traits_defaults():
    actor = groups.group_list()
    group = actor()  # Component instance
    assert group.__class__ == groups.GroupList.GroupList
    assert group.enabled == False
    assert group.options == []


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    group = test_subject.group
    assert group.__class__ == groups.GroupList.GroupList
    assert group.enabled == True
    assert group.options == [("yes", "1"), ("no", "2")]
