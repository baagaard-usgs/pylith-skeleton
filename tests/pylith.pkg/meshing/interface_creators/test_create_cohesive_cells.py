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
from pylith.meshing import interface_creators


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_create_cohesive_cells.yaml")


def test_traits_defaults():
    actor = interface_creators.create_cohesive_cells()
    mesher = actor()  # Component instance
    assert mesher.__class__ == interface_creators.CreateCohesiveCells.CreateCohesiveCells


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    mesher = test_subject.mesher
    assert mesher.__class__ == interface_creators.CreateCohesiveCells.CreateCohesiveCells


# End of file
