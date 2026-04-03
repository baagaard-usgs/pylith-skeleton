import pathlib

import pytest

import pylith
from pylith import application_defaults


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_simulation_defaults.yaml")


def test_traits_defaults():
    app_defaults = application_defaults.simulation_defaults()  # Actor
    assert app_defaults().__class__ == application_defaults.SimulationDefaults.SimulationDefaults
    assert str(app_defaults.output_dir) == "output"
    assert app_defaults.output_name is None
    assert app_defaults.quadrature_order == 1
    assert app_defaults.output_basis_order == 1


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    app_defaults = test_subject.app_defaults
    assert app_defaults.__class__ == application_defaults.SimulationDefaults.SimulationDefaults
    assert str(app_defaults.output_dir) == "sim_output"
    assert app_defaults.output_name == "step01"
    assert app_defaults.quadrature_order == 0
    assert app_defaults.output_basis_order == 0
