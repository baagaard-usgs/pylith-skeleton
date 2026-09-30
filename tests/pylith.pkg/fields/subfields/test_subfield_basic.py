import pathlib

import pytest

import pylith
from pylith.fields import subfields


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_subfield_basic.yaml")


def test_traits_defaults():
    actor = subfields.basic()
    subfield = actor()  # Component instance
    assert subfield.__class__ == subfields.SubfieldBasic.SubfieldBasic
    assert subfield.alias is None

    discretization = subfield.discretization
    assert discretization.basis_order is None


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    subfield = test_subject.subfield
    assert subfield.__class__ == subfields.SubfieldBasic.SubfieldBasic
    assert subfield.alias == "bulky_modulus"

    discretization = subfield.discretization
    assert discretization.basis_order == 2
