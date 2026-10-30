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
from pylith import mesh_io


@pytest.fixture
def load_yaml():
    cur_path = pyre.primitives.path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_ascii.yaml")


def test_traits_defaults():
    actor = mesh_io.ascii()
    reader = actor()  # Component instance
    assert reader.__class__ == mesh_io.MeshIOAscii.MeshIOAscii
    assert reader.uri is None


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    reader = test_subject.mesh_io
    assert reader.__class__ == mesh_io.MeshIOAscii.MeshIOAscii
    assert str(reader.uri) == "mesh.txt"


# End of file
