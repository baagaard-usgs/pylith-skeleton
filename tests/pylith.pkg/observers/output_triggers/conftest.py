import pytest

import pylith
from pylith.protocols.observers import output_trigger


@pytest.fixture
def local_test_subject():
    yield LocalTestSubject
    pylith.reset()


class LocalTestSubject(pylith.component):

    trigger = output_trigger()
