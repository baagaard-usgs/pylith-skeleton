import pathlib

import pytest

import spatialdata
from spatialdata import coordinate_systems


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    spatialdata.loadConfiguration(cur_path / "test_geographic_local.yaml")


def test_traits_defaults():
    cs = coordinate_systems.geographic_local() # Actor
    assert cs().__class__ == coordinate_systems.GeographicLocal.GeographicLocal
    assert cs.crs_string == "EPSG:4326"
    assert cs.space_dim == 3
    assert cs.origin_x == 0.0
    assert cs.origin_y == 0.0
    assert cs.y_azimuth == 0.0


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    cs = test_subject.cs
    assert cs.__class__ == coordinate_systems.GeographicLocal.GeographicLocal
    assert cs.crs_string == "EPSG:5678"
    assert cs.space_dim == 2
    assert cs.origin_x == 1.0
    assert cs.origin_y == 2.0
    assert cs.y_azimuth == 3.0
