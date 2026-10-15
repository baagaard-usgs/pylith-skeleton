# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2026 All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================

import pathlib

import pytest

import pylith
from pylith.mesh_initializers import reorderings


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_petsc_reordering.yaml")


def test_traits_defaults():
    actor = reorderings.petsc()
    reordering = actor()  # Component instance
    assert reordering.__class__ == reorderings.ReorderingPetsc.ReorderingPetsc


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    reordering = test_subject.reordering
    assert reordering.__class__ == reorderings.ReorderingPetsc.ReorderingPetsc


# End of file
