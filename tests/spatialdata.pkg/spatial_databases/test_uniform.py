import pathlib

import pytest

import spatialdata
from spatialdata import spatial_databases
from pyre.units.length import km
from pyre.units.time import second


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    spatialdata.loadConfiguration(cur_path / "test_uniform.yaml")


def test_traits_defaults():
    db = spatial_databases.uniform() # Actor
    assert db().__class__ == spatial_databases.Uniform.Uniform
    assert db.values == []


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    db = test_subject.db
    assert db.__class__ == spatial_databases.Uniform.Uniform
    assert len(db.values) == 2

    value = db.values[0]
    assert value.name == "vp"
    assert str(value.value) == str(4.0 * km / second)

    value = db.values[1]
    assert value.name == "vs"
    assert str(value.value) == str(2.7 * km / second)
