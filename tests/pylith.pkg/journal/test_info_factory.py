import pytest

import pylith.journal


@pytest.fixture
def factory():
    yield pylith.journal.info_factory()


def test_about(factory):
    about = factory.about()
    assert about.name == "about"
    assert about.severity == "info"


def test_application_flow(factory):
    application_flow = factory.application_flow(detail=2)
    assert application_flow.name == "application-flow"
    assert application_flow.severity == "info"
    assert application_flow.detail == 2

    application_flow = factory.application_flow_all(detail=3)
    assert application_flow.name == "application-flow-all"
    assert application_flow.severity == "info"
    assert application_flow.detail == 3


def test_debug_config(factory):
    debug_config = factory.debug_config()
    assert debug_config.name == "debug-config"
    assert debug_config.severity == "info"


def test_initialization(factory):
    initialization = factory.initialization()
    assert initialization.name == "initialization"
    assert initialization.severity == "info"
    assert initialization.detail == 5

    initialization = factory.initialization(detail=2)
    assert initialization.name == "initialization"
    assert initialization.severity == "info"
    assert initialization.detail == 2
