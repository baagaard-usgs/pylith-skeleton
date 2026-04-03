import pathlib

import pytest

from pyre.units.length import meter

import pylith
from pylith import interior_interfaces


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_fault_impulses.yaml")


def test_traits_defaults():
    fault = interior_interfaces.fault_cohesive_impulses()  # Actor
    assert fault().__class__.__name__ == "FaultCohesiveImpulses"
    assert fault.label_name is None
    assert fault.label_value == 1
    assert fault.edge_label_name is None
    assert fault.edge_label_value == 1
    assert fault.ref_dir_1 == [0.0, 0.0, 1.0]
    assert fault.ref_dir_2 == [0.0, 1.0, 0.0]
    assert fault.threshold == 1.0e-3 * meter
    assert fault.impulse_dof == []


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    fault = test_subject.interface
    assert fault.__class__.__name__ == "FaultCohesiveImpulses"
    assert fault.label_name == "impulse_fault"
    assert fault.label_value == 2
    assert fault.edge_label_name == "edge_impulse"
    assert fault.edge_label_value == 3
    assert fault.ref_dir_1 == [0.0, 1.0, 0.0]
    assert fault.ref_dir_2 == [1.0, 0.0, 0.0]
    assert fault.threshold == 2.0e-3 * meter
    assert fault.impulse_dof == [0, 1]
