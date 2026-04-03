import pathlib

import pytest

from pyre.units.length import km, meter
from pyre.units.pressure import GPa, pascal
from pyre.units.time import second

import pylith
from pylith import scales


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_quasistatic_poroelasticity.yaml")


def test_traits_defaults():
    scales_component = scales.quasistatic_poroelasticity() # Actor
    assert scales_component().__class__ == scales.QuasistaticPoroelasticity.QuasistaticPoroelasticity
    assert scales_component.length_scale == 100.0 * km
    assert scales_component.displacement_scale == 1.0 * meter
    assert scales_component.shear_modulus == 10.0 * GPa
    assert scales_component.viscosity == 0.001 * pascal * second
    assert scales_component.permeability == 1.0e-13 * meter**2


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    scales_component = test_subject.scales
    assert scales_component.__class__ == scales.QuasistaticPoroelasticity.QuasistaticPoroelasticity
    assert scales_component.length_scale == 50.0 * km
    assert scales_component.displacement_scale == 0.5 * meter
    assert scales_component.shear_modulus == 5.0 * GPa
    assert scales_component.viscosity == 0.0005 * pascal * second
    assert scales_component.permeability == 5.0e-14 * meter**2