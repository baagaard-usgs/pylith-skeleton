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
    poroelasticity_scales = scales.quasistatic_poroelasticity() # Actor
    assert poroelasticity_scales().__class__ == scales.QuasistaticPoroelasticity.QuasistaticPoroelasticity
    assert poroelasticity_scales.length_scale == 100.0 * km
    assert poroelasticity_scales.displacement_scale == 1.0 * meter
    assert poroelasticity_scales.shear_modulus == 10.0 * GPa
    assert poroelasticity_scales.viscosity == 0.001 * pascal * second
    assert poroelasticity_scales.permeability == 1.0e-13 * meter**2


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    poroelasticity_scales = test_subject.scales
    assert poroelasticity_scales.__class__ == scales.QuasistaticPoroelasticity.QuasistaticPoroelasticity
    assert poroelasticity_scales.length_scale == 50.0 * km
    assert poroelasticity_scales.displacement_scale == 0.5 * meter
    assert poroelasticity_scales.shear_modulus == 5.0 * GPa
    assert poroelasticity_scales.viscosity == 0.0005 * pascal * second
    assert poroelasticity_scales.permeability == 5.0e-14 * meter**2