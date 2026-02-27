import pathlib

import pytest

import spatialdata
from spatialdata import coordinate_systems


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    spatialdata.loadConfiguration(cur_path / "test_geographic.yaml")


def test_traits_defaults():
    cs = coordinate_systems.geographic()
    assert cs.__class__ == coordinate_systems.Geographic.Geographic
    assert cs.crs_string == "EPSG:4326"
    assert cs.space_dim == 3


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    cs = test_subject.cs
    assert cs.__class__ == coordinate_systems.Geographic.Geographic
    assert cs.crs_string == "EPSG:1234"
    assert cs.space_dim == 2
