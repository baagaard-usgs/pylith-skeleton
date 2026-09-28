import pytest

import pylith.journal


@pytest.fixture
def factory():
    yield pylith.journal.firewall_factory()


def test_internal_error(factory):
    internal_error = factory.internal_error()
    assert internal_error.name == "internal-error"
    assert internal_error.severity == "firewall"


def test_logic_error(factory):
    logic_error = factory.logic_error()
    assert logic_error.name == "logic-error"
    assert logic_error.severity == "firewall"
