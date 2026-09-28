import pathlib

import pytest

import pylith
from pylith.petsc import options
from pylith.petsc.options import groups


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_simulation_options.yaml")


def test_traits_defaults():
    actor = options.simulation_options()
    options_manager = actor()  # Component instance
    assert options_manager.__class__ == pylith.petsc.options.SimulationOptions.SimulationOptions

    testing = options_manager.testing
    assert testing.__class__ == groups.GroupList.GroupList
    assert testing.enabled == False
    assert testing.options == []

    collective_io = options_manager.collective_io
    assert collective_io.__class__ == groups.GroupList.GroupList
    assert collective_io.enabled == False
    assert collective_io.options == []

    attach_debugger = options_manager.attach_debugger
    assert attach_debugger.__class__ == groups.GroupList.GroupList
    assert attach_debugger.enabled == False
    assert attach_debugger.options == []


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    options_manager = test_subject.options_manager
    assert options_manager.__class__ == pylith.petsc.options.SimulationOptions.SimulationOptions

    testing = options_manager.testing
    assert testing.__class__ == groups.GroupList.GroupList
    assert testing.enabled == True
    assert testing.options == [("malloc_debug",)]

    collective_io = options_manager.collective_io
    assert collective_io.__class__ == groups.GroupList.GroupList
    assert collective_io.enabled == False
    assert collective_io.options == [("viewer_hdf5_collective",)]

    attach_debugger = options_manager.attach_debugger
    assert attach_debugger.__class__ == groups.GroupList.GroupList
    assert attach_debugger.enabled == True
    assert attach_debugger.options == [
        ("stop_for_debugger",),
        ("debugger_pause", "10"),
        ("malloc_debug", "False"),
        ("check_pointer_intensity", "False"),
    ]
