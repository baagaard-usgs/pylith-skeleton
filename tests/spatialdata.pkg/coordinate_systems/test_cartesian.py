import pathlib

import pytest

import spatialdata
from spatialdata import coordinate_systems
from pyre.units.length import meter, kilometer


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    spatialdata.loadConfiguration(cur_path / "test_cartesian.yaml")


def test_traits_defaults():
    cs = coordinate_systems.cartesian()
    assert cs.__class__ == coordinate_systems.Cartesian.Cartesian
    assert cs.units == meter
    assert cs.space_dim == 3


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    cs = test_subject.cs
    assert cs.__class__ == coordinate_systems.Cartesian.Cartesian
    assert cs.units == kilometer
    assert cs.space_dim == 2
