import pytest

import pylith
from pylith.protocols import petsc


@pytest.fixture
def local_test_subject():
    yield LocalTestSubject
    pylith.reset()


class LocalTestSubject(pylith.component):

    options_manager = petsc.options_manager()
