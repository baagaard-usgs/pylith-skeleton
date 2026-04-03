import pytest

import pylith
from pylith import protocols


@pytest.fixture
def local_test_subject():
    yield LocalTestSubject
    pylith.reset()


class LocalTestSubject(pylith.component):

    writer = protocols.data_writer()
