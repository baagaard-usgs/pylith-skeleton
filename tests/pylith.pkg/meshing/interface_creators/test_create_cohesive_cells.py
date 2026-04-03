import pathlib

import pytest

import pylith
from pylith.meshing import interface_creators


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_create_cohesive_cells.yaml")


def test_traits_defaults():
    mesher = interface_creators.create_cohesive_cells()  # Actor
    assert mesher().__class__ == interface_creators.CreateCohesiveCells.CreateCohesiveCells


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    mesher = test_subject.mesher
    assert mesher.__class__ == interface_creators.CreateCohesiveCells.CreateCohesiveCells
