import pathlib

import pytest

import pylith
from pylith import data_writers


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_hdf5.yaml")


def test_traits_defaults():
    writer = data_writers.hdf5()  # Actor
    assert writer().__class__ == data_writers.DataWriterHDF5.DataWriterHDF5
    assert writer.uri is None


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    writer = test_subject.writer
    assert writer.__class__ == data_writers.DataWriterHDF5.DataWriterHDF5
    assert str(writer.uri) == "test.h5"
