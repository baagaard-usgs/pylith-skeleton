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

import spatialdata
from spatialdata import points_io


@pytest.fixture
def load_yaml():
    cur_path = pyre.primitives.path(__file__).parent
    spatialdata.loadConfiguration(cur_path / "test_points_stream.yaml")


def test_traits_defaults():
    actor = points_io.stream()
    stations = actor()  # Component instance
    assert stations.__class__ == points_io.Stream.Stream
    assert stations.uri is None
    assert stations.comment_flag == "#"
    assert stations.format == "%14.5e"


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    stations = test_subject.stations
    assert stations.__class__ == points_io.Stream.Stream
    assert str(stations.uri) == "gnss_stations.txt"
    assert stations.comment_flag == "%"
    assert stations.format == "%7.4f"


# End of file
