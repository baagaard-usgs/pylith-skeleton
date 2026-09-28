import pytest

import pylith.journal


@pytest.fixture
def factory():
    yield pylith.journal.error_factory()


def test_configuration_error(factory):
    configuration_error = factory.configuration_error()
    assert configuration_error.name == "configuration-error"
    assert configuration_error.severity == "error"


def test_input_error(factory):
    input_error = factory.input_error()
    assert input_error.name == "input-error"
    assert input_error.severity == "error"


def test_external_error(factory):
    external_error = factory.external_error()
    assert external_error.name == "external-error"
    assert external_error.severity == "error"
