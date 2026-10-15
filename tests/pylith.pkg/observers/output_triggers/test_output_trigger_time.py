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

from pyre.units.time import year

import pylith
from pylith.observers import output_triggers


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_output_trigger_time.yaml")


def test_traits_defaults():
    actor = output_triggers.time()
    trigger = actor()  # Component instance
    assert trigger.__class__ == output_triggers.OutputTriggerTime.OutputTriggerTime
    assert trigger.elapsed_time == 0 * year


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")  # Component instance
    trigger = test_subject.trigger
    assert trigger.__class__ == output_triggers.OutputTriggerTime.OutputTriggerTime
    assert trigger.elapsed_time == 3 * year


# End of file
