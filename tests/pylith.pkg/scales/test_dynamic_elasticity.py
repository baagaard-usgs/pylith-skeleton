import pathlib

import pytest

from pyre.units.length import km, meter
from pyre.units.mass import kg
from pyre.units.time import second

import pylith
from pylith import scales


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_dynamic_elasticity.yaml")


def test_traits_defaults():
    scales_component = scales.dynamic_elasticity() # Actor
    assert scales_component().__class__ == scales.DynamicElasticity.DynamicElasticity
    assert scales_component.length_scale == 100.0 * km
    assert scales_component.displacement_scale == 1.0 * meter
    assert scales_component.density == 2500.0 * kg / meter**3
    assert scales_component.shear_wave_speed == 3.0 * km / second


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    scales_component = test_subject.scales
    assert scales_component.__class__ == scales.DynamicElasticity.DynamicElasticity
    assert scales_component.length_scale == 50.0 * km
    assert scales_component.displacement_scale == 0.5 * meter
    assert scales_component.density == 2000.0 * kg / meter**3
    assert scales_component.shear_wave_speed == 2.5 * km / second