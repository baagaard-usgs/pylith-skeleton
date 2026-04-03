import pathlib

import pytest

import pylith
from pylith.mesh_initializers import distributors

from pylith import data_writers

@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_petsc_distributor.yaml")


def test_traits_defaults():
    distributor = distributors.petsc()  # Actor
    assert distributor().__class__ == distributors.DistributorPetsc.DistributorPetsc
    assert distributor.partitioner == "parmetis"
    assert distributor.use_edge_weighting is True
    assert distributor.write_partition is False
    assert distributor.data_writer().__class__ == data_writers.DataWriterHDF5.DataWriterHDF5


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    distributor = test_subject.distributor
    assert distributor.__class__ == distributors.DistributorPetsc.DistributorPetsc
    assert distributor.partitioner == "simple"
    assert distributor.use_edge_weighting is False
    assert distributor.write_partition is True
    assert distributor.data_writer.__class__ == data_writers.DataWriterHDF5.DataWriterHDF5
