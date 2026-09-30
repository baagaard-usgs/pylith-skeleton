import pathlib

import pytest

import pylith
from pylith import observers


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_output_physics.yaml")


def test_traits_defaults():
    actor = observers.output_physics()
    observer = actor()  # Component instance
    assert observer.__class__ == observers.OutputPhysics.OutputPhysics
    assert observer.output_basis_order == 1
    assert observer.refine_levels == 0
    assert observer.info_fields == ["all"]
    assert observer.data_fields == ["all"]

    trigger = observer.trigger
    assert trigger.__class__ == pylith.observers.output_triggers.OutputTriggerStep.OutputTriggerStep

    writer = observer.writer
    assert writer.__class__ == pylith.data_writers.DataWriterHDF5.DataWriterHDF5


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")  # Component instance
    observer = test_subject.observer
    assert observer.__class__ == observers.OutputPhysics.OutputPhysics
    assert observer.output_basis_order == 0
    assert observer.refine_levels == 2
    assert observer.info_fields == ["shear_modulus", "bulk_modulus"]
    assert observer.data_fields == ["cauchy_stress", "cauchy_strain"]

    trigger = observer.trigger
    assert trigger.__class__ == pylith.observers.output_triggers.OutputTriggerStep.OutputTriggerStep

    writer = observer.writer
    assert writer.__class__ == pylith.data_writers.DataWriterHDF5.DataWriterHDF5
