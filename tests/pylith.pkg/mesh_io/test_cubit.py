import pathlib

import pytest

import pylith
from pylith import mesh_io


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_cubit.yaml")


def test_traits_defaults():
    reader = mesh_io.cubit()  # Actor
    assert reader().__class__ == mesh_io.MeshIOCubit.MeshIOCubit
    assert reader.uri is None


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    reader = test_subject.mesh_io
    assert reader.__class__ == mesh_io.MeshIOCubit.MeshIOCubit
    assert str(reader.uri) == "mesh.exo"
