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
from pylith.interior_interfaces import source_time_fns


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_kinsrc_time_history.yaml")


def test_traits_defaults():
    actor = source_time_fns.time_history()
    source_fn = actor()  # Component instance
    assert source_fn.__class__ == source_time_fns.TimeHistory.TimeHistory


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    source_fn = test_subject.source_fn
    assert source_fn.__class__ == source_time_fns.TimeHistory.TimeHistory


# End of file
