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
from spatialdata import time_histories


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    spatialdata.loadConfiguration(cur_path / "test_points.yaml")


def test_traits_defaults():
    th = time_histories.points()  # Actor
    assert th().__class__ == time_histories.Points.Points
    assert th.description is None
    assert th.uri is None


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    th = test_subject.time_history
    assert th.__class__ == time_histories.Points.Points
    assert th.description == "Slip time history"
    assert str(th.uri) == "slip.timedb"


# End of file
