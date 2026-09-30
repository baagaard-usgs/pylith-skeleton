import pytest

import pylith.journal


@pytest.fixture
def factory():
    yield pylith.journal.debug_factory()


def test_application_flow(factory):
    application_flow = factory.application_flow()
    assert application_flow.name == "application-flow"
    assert application_flow.severity == "debug"


def test_auxiliary_fields(factory):
    auxiliary_fields = factory.auxiliary_fields()
    assert auxiliary_fields.name == "auxiliary-fields"
    assert auxiliary_fields.severity == "debug"


def test_integration_kernels(factory):
    integration_kernels = factory.integration_kernels()
    assert integration_kernels.name == "integration-kernels"
    assert integration_kernels.severity == "debug"


def test_mesh(factory):
    mesh = factory.mesh()
    assert mesh.name == "mesh"
    assert mesh.severity == "debug"


def test_mms_test(factory):
    mms_test = factory.mms_test()
    assert mms_test.name == "mms-test"
    assert mms_test.severity == "debug"


def test_solver(factory):
    solver = factory.solver()
    assert solver.name == "solver"
    assert solver.severity == "debug"


def test_todo(factory):
    todo = factory.todo()
    assert todo.name == "TODO"
    assert todo.severity == "debug"
