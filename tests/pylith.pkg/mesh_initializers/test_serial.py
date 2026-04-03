import pathlib

import pytest

import pylith
from pylith import mesh_initializers, mesh_io

from pylith.mesh_initializers import reorderings, distributors
from pylith.meshing import interface_creators, refiners

@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_serial.yaml")


def test_traits_defaults():
    initializer = mesh_initializers.serial()  # Actor
    assert initializer().__class__ == mesh_initializers.InitializerSerial.InitializerSerial
    assert initializer.read_mesh().__class__ == mesh_io.MeshIOPetsc.MeshIOPetsc
    assert initializer.reorder_mesh().__class__ == reorderings.ReorderingPetsc.ReorderingPetsc
    assert initializer.distribute_mesh().__class__ == distributors.DistributorPetsc.DistributorPetsc
    assert initializer.insert_interface().__class__ == interface_creators.CreateCohesiveCells.CreateCohesiveCells
    assert initializer.refine_mesh().__class__ == refiners.RefineUniform.RefineUniform


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    initializer = test_subject.initializer
    assert initializer.__class__ == mesh_initializers.InitializerSerial.InitializerSerial
    assert initializer.read_mesh.__class__ == mesh_io.MeshIOAscii.MeshIOAscii
    assert initializer.reorder_mesh.__class__ == reorderings.ReorderingPetsc.ReorderingPetsc
    assert initializer.distribute_mesh.__class__ == distributors.DistributorPetsc.DistributorPetsc
    assert initializer.insert_interface.__class__ == interface_creators.CreateCohesiveCells.CreateCohesiveCells
    assert initializer.refine_mesh.__class__ == refiners.RefineUniform.RefineUniform
