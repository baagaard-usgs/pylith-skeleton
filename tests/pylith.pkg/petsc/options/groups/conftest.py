import pytest

import pylith
from pylith.protocols.petsc.options import groups


@pytest.fixture
def local_test_subject():
    yield LocalTestSubject
    pylith.reset()


class LocalTestSubject(pylith.component):

    group = groups.group()
