import pathlib

import pytest

import spatialdata
from spatialdata import spatial_databases


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    spatialdata.loadConfiguration(cur_path / "test_simple_grid.yaml")


def test_traits_defaults():
    db = spatial_databases.simple_grid()
    assert db.__class__ == spatial_databases.SimpleGrid.SimpleGrid
    assert db.uri is None
    assert db.query_type == "linear"


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    db = test_subject.db
    assert db.__class__ == spatial_databases.SimpleGrid.SimpleGrid
    assert str(db.uri) == "velocity.spatialdb"
    assert db.query_type == "nearest"
