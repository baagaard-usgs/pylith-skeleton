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
from spatialdata import spatial_databases


@pytest.fixture
def load_yaml():
    cur_path = pyre.primitives.path(__file__).parent
    spatialdata.loadConfiguration(cur_path / "test_simple_grid.yaml")


def test_traits_defaults():
    actor = spatial_databases.simple_grid()
    db = actor()  # Component instance
    assert db.__class__ == spatial_databases.SimpleGrid.SimpleGrid
    assert db.uri is None
    assert db.query_type == "linear"


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    db = test_subject.db
    assert db.__class__ == spatial_databases.SimpleGrid.SimpleGrid
    assert str(db.uri) == "velocity.spatialdb"
    assert db.query_type == "nearest"


# End of file
