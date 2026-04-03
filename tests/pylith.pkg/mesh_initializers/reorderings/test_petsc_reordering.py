import pathlib

import pytest

import pylith
from pylith.mesh_initializers import reorderings


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_petsc_reordering.yaml")


def test_traits_defaults():
    reordering = reorderings.petsc()  # Actor
    assert reordering().__class__ == reorderings.ReorderingPetsc.ReorderingPetsc


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    reordering = test_subject.reordering
    assert reordering.__class__ == reorderings.ReorderingPetsc.ReorderingPetsc
