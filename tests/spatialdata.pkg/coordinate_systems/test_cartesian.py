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
from spatialdata import coordinate_systems
from pyre.units.length import meter, kilometer


@pytest.fixture
def load_yaml():
    cur_path = pyre.primitives.path(__file__).parent
    spatialdata.loadConfiguration(cur_path / "test_cartesian.yaml")


def test_traits_defaults():
    actor = coordinate_systems.cartesian()
    cs = actor()  # Component instance
    assert cs.__class__ == coordinate_systems.Cartesian.Cartesian
    assert cs.units == meter
    assert cs.space_dim == 3


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    cs = test_subject.cs
    assert cs.__class__ == coordinate_systems.Cartesian.Cartesian
    assert cs.units == kilometer
    assert cs.space_dim == 2


# End of file
