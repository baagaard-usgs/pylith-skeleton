import pathlib

import pytest

import spatialdata
from spatialdata import spatial_databases
from pyre.units.length import km


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    spatialdata.loadConfiguration(cur_path / "test_composite.yaml")


def test_traits_defaults():
    db = spatial_databases.composite()
    assert db.__class__ == spatial_databases.Composite.Composite
    assert db.databases == []


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    composite = test_subject.db
    assert composite.__class__ == spatial_databases.Composite.Composite
    assert len(composite.databases) == 2

    db = composite.databases[0]
    assert db.values == ["vp", "vs", "density"]
    assert db.database.__class__ == spatial_databases.SimpleGrid.SimpleGrid
    assert str(db.database.uri) == "elastic.spatialdb"
    assert db.database.query_type == "nearest"

    db = composite.databases[1]
    assert db.values == ["viscosity"]
    assert db.database.__class__ == spatial_databases.Simple.Simple
    assert str(db.database.uri) == "viscoelastic.spatialdb"
    assert db.database.query_type == "linear"
