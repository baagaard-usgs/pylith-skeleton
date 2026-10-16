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
from pylith.meshing import refiners


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_refine_uniform.yaml")


def test_traits_defaults():
    actor = refiners.uniform()
    refiner = actor()  # Component instance
    assert refiner.__class__ == refiners.RefineUniform.RefineUniform
    assert refiner.levels == 0


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    refiner = test_subject.refiner
    assert refiner.__class__ == refiners.RefineUniform.RefineUniform
    assert refiner.levels == 2


# End of file
