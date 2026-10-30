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
from pylith.observers import output_triggers


@pytest.fixture
def load_yaml():
    cur_path = pyre.primitives.path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_output_trigger_step.yaml")


def test_traits_defaults():
    actor = output_triggers.step()
    trigger = actor()  # Component instance
    assert trigger.__class__ == output_triggers.OutputTriggerStep.OutputTriggerStep
    assert trigger.num_skip == 0


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")  # Component instance
    trigger = test_subject.trigger
    assert trigger.__class__ == output_triggers.OutputTriggerStep.OutputTriggerStep
    assert trigger.num_skip == 5


# End of file
