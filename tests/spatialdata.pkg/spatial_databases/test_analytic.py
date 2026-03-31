import pathlib

import pytest

import spatialdata
from spatialdata import spatial_databases
from pyre.units.length import meter, km
from pyre.units.time import second


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    spatialdata.loadConfiguration(cur_path / "test_analytic.yaml")


def test_traits_defaults():
    db = spatial_databases.analytic() # Actor
    assert db().__class__ == spatial_databases.Analytic.Analytic
    assert db.values == []


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    db = test_subject.db
    assert db.__class__ == spatial_databases.Analytic.Analytic
    assert len(db.values) == 2

    value = db.values[0]
    assert value.name == "vp"
    assert value.units == km / second
    assert value.expression == "x"
    assert value.coord_sys.pyre_family() == "spatialdata.coordinate_systems.cartesian"

    value = db.values[1]
    assert value.name == "vs"
    assert value.units == meter / second
    assert value.expression == "x + y"
    assert value.coord_sys.pyre_family() == "spatialdata.coordinate_systems.geographic"
