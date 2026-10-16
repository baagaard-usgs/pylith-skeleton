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
    spatialdata.loadConfiguration(cur_path / "test_geographic_local.yaml")


def test_traits_defaults():
    actor = coordinate_systems.geographic_local()
    cs = actor()  # Component instance
    assert cs.__class__ == coordinate_systems.GeographicLocal.GeographicLocal
    assert cs.crs_string == "EPSG:4326"
    assert cs.space_dim == 3
    assert cs.origin_x == 0.0
    assert cs.origin_y == 0.0
    assert cs.y_azimuth == 0.0


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    cs = test_subject.cs
    assert cs.__class__ == coordinate_systems.GeographicLocal.GeographicLocal
    assert cs.crs_string == "EPSG:5678"
    assert cs.space_dim == 2
    assert cs.origin_x == 1.0
    assert cs.origin_y == 2.0
    assert cs.y_azimuth == 3.0


# End of file
