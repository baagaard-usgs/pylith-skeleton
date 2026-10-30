# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2026 All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================

import pytest

import pyre

import pylith
from pylith import mesh_initializers, mesh_io

from pylith.mesh_initializers import reorderings, distributors
from pylith.meshing import interface_creators, refiners


@pytest.fixture
def load_yaml():
    cur_path = pyre.primitives.path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_parallel.yaml")


def test_traits_defaults():
    actor = mesh_initializers.parallel()
    initializer = actor()  # Component instance
    assert initializer.__class__ == mesh_initializers.InitializerParallel.InitializerParallel
    assert initializer.read_mesh.__class__ == mesh_io.MeshIOPetsc.MeshIOPetsc
    assert initializer.distribute_mesh.__class__ == distributors.DistributorPetsc.DistributorPetsc
    assert initializer.insert_interface.__class__ == interface_creators.CreateCohesiveCells.CreateCohesiveCells
    assert initializer.refine_mesh.__class__ == refiners.RefineUniform.RefineUniform


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    initializer = test_subject.initializer
    assert initializer.__class__ == mesh_initializers.InitializerParallel.InitializerParallel
    assert initializer.read_mesh.__class__ == mesh_io.MeshIOAscii.MeshIOAscii
    assert initializer.distribute_mesh.__class__ == distributors.DistributorPetsc.DistributorPetsc
    assert initializer.insert_interface.__class__ == interface_creators.CreateCohesiveCells.CreateCohesiveCells
    assert initializer.refine_mesh.__class__ == refiners.RefineUniform.RefineUniform


# End of file
