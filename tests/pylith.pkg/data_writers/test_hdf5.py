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

import pylith
from pylith import data_writers


@pytest.fixture
def load_yaml():
    cur_path = pyre.primitives.path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_hdf5.yaml")


def test_traits_defaults():
    actor = data_writers.hdf5()
    writer = actor()  # Component instance
    assert writer.__class__ == data_writers.DataWriterHDF5.DataWriterHDF5
    assert writer.uri is None


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    writer = test_subject.writer
    assert writer.__class__ == data_writers.DataWriterHDF5.DataWriterHDF5
    assert str(writer.uri) == "test.h5"


# End of file
