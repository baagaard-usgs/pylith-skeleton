import pathlib

import pytest

import spatialdata
from spatialdata import spatial_databases
from pyre.units.length import meter
from pyre.units.time import second


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    spatialdata.loadConfiguration(cur_path / "test_gravity_field.yaml")


def test_traits_defaults():
    db = spatial_databases.gravity_field()
    assert db.__class__ == spatial_databases.GravityField.GravityField
    assert db.gravity_dir == [0.0, 0.0, -1.0]
    assert str(db.acceleration) == str(9.80665 * meter / second)


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    db = test_subject.db
    assert db.__class__ == spatial_databases.GravityField.GravityField
    assert db.gravity_dir == [0.0, -1.0, 0.0]
    assert str(db.acceleration) == str(4.5 * meter / second)
