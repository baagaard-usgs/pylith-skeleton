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

import spatialdata
from spatialdata import coordinate_systems


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    spatialdata.loadConfiguration(cur_path / "test_geographic.yaml")


def test_traits_defaults():
    actor = coordinate_systems.geographic()
    cs = actor()  # Component instance
    assert cs.__class__ == coordinate_systems.Geographic.Geographic
    assert cs.crs_string == "EPSG:4326"
    assert cs.space_dim == 3


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    cs = test_subject.cs
    assert cs.__class__ == coordinate_systems.Geographic.Geographic
    assert cs.crs_string == "EPSG:1234"
    assert cs.space_dim == 2


# End of file
