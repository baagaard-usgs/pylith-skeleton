import pathlib

import pytest

import pylith
from pylith import mesh_initializers


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_petsc.yaml")


def test_traits_defaults():
    distributor = mesh_initializers.distributors.petsc()  # Actor
    assert distributor().__class__.__name__ == "DistributorPetsc"
    assert distributor.partitioner == "parmetis"
    assert distributor.use_edge_weighting is True
    assert distributor.write_partition is False


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    distibutor = test_subject.distributor
    assert distibutor.__class__.__name__ == "DistributorPetsc"
    assert distibutor.partitioner == "simple"
    assert distibutor.use_edge_weighting is False
    assert distibutor.write_partition is True
