import pathlib

import pytest

import pylith
from pylith import mesh_io


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_petsc.yaml")


def test_traits_defaults():
    reader = mesh_io.petsc()  # Actor
    assert reader().__class__ == mesh_io.MeshIOPetsc.MeshIOPetsc
    assert reader.uri is None
    assert reader.gmsh_mark_recursive == False
    assert reader.petsc_options_prefix == ""


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    reader = test_subject.mesh_io
    assert reader.__class__ == mesh_io.MeshIOPetsc.MeshIOPetsc
    assert reader.uri == "mesh.h5"
    assert reader.gmsh_mark_recursive == True
    assert reader.petsc_options_prefix == "mesh_"
