import pathlib

import pytest

from pyre.units.length import km, meter
from pyre.units.pressure import GPa
from pyre.units.time import year

import pylith
from pylith import scales


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_quasistatic_elasticity.yaml")


def test_traits_defaults():
    elasticity_scales = scales.quasistatic_elasticity() # Actor
    assert elasticity_scales().__class__ == scales.QuasistaticElasticity.QuasistaticElasticity
    assert elasticity_scales.length_scale == 100.0 * km
    assert elasticity_scales.displacement_scale == 1.0 * meter
    assert elasticity_scales.shear_modulus == 10.0 * GPa
    assert elasticity_scales.time_scale == 100.0 * year


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    elasticity_scales = test_subject.scales
    assert elasticity_scales.__class__ == scales.QuasistaticElasticity.QuasistaticElasticity
    assert elasticity_scales.length_scale == 50.0 * km
    assert elasticity_scales.displacement_scale == 0.5 * meter
    assert elasticity_scales.shear_modulus == 5.0 * GPa
    assert elasticity_scales.time_scale == 50.0 * year