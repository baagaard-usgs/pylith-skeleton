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
    elasticity_scales = scales.dynamic_elasticity() # Actor
    assert elasticity_scales().__class__ == scales.DynamicElasticity.DynamicElasticity
    assert elasticity_scales.length_scale == 100.0 * km
    assert elasticity_scales.displacement_scale == 1.0 * meter
    assert elasticity_scales.density == 2500.0 * kg / meter**3
    assert elasticity_scales.shear_wave_speed == 3.0 * km / second


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    elasticity_scales = test_subject.scales
    assert elasticity_scales.__class__ == scales.DynamicElasticity.DynamicElasticity
    assert elasticity_scales.length_scale == 50.0 * km
    assert elasticity_scales.displacement_scale == 0.5 * meter
    assert elasticity_scales.density == 2000.0 * kg / meter**3
    assert elasticity_scales.shear_wave_speed == 2.5 * km / second