import pytest

import pylith
from pylith import protocols


@pytest.fixture
def local_test_subject():
    yield LocalTestSubject
    pylith.reset()


class LocalTestSubject(pylith.component):

    mesh_io = protocols.mesh_io()