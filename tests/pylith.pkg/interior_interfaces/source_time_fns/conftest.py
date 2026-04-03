import pytest

import pylith
from pylith.protocols.interior_interfaces import source_time_fn


@pytest.fixture
def local_test_subject():
    yield LocalTestSubject
    pylith.reset()


class LocalTestSubject(pylith.component):

    source_fn = source_time_fn()
