import pytest

import pylith
from pylith.protocols import mesh_initializers


@pytest.fixture
def local_test_subject():
    yield LocalTestSubject
    pylith.reset()


class LocalTestSubject(pylith.component):

    reordering = mesh_initializers.reordering()