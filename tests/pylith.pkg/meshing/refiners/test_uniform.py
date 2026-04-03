import pathlib

import pytest

import pylith
from pylith import meshing


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_uniform.yaml")


def test_traits_defaults():
    refiner = meshing.refiners.uniform()  # Actor
    assert refiner().__class__ == meshing.refiners.RefineUniform.RefineUniform
    assert refiner.levels == 0


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    refiner = test_subject.refiner
    assert refiner.__class__ == meshing.refiners.RefineUniform.RefineUniform
    assert refiner.levels == 2
