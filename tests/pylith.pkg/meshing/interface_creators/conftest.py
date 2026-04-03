import pytest

import pylith
from pylith.protocols import meshing


@pytest.fixture
def local_test_subject():
    yield LocalTestSubject
    pylith.reset()


class LocalTestSubject(pylith.component):

    mesher = meshing.interface_creator()
