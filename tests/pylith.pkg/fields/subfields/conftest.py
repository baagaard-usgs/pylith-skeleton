import pytest

import pylith
from pylith.protocols import fields


@pytest.fixture
def local_test_subject():
    yield LocalTestSubject
    pylith.reset()


class LocalTestSubject(pylith.component):

    subfield = fields.subfield()
