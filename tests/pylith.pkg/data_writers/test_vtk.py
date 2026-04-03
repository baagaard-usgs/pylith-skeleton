import pathlib

import pytest

import pylith
from pylith import data_writers
from pyre.units.time import second, year


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_vtk.yaml")


def test_traits_defaults():
    writer = data_writers.vtk()  # Actor
    assert writer().__class__ == data_writers.DataWriterVTK.DataWriterVTK
    assert writer.uri is None
    assert writer.time_format == "%f"
    assert writer.time_scale == 1.0 * second
    assert writer.float_precision == 6


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    writer = test_subject.writer
    assert writer.__class__ == data_writers.DataWriterVTK.DataWriterVTK
    assert str(writer.uri) == "test.vtu"
    assert writer.time_format == "%14.4e"
    assert writer.time_scale == 1.0 * year
    assert writer.float_precision == 4
