import pytest

import spatialdata
from spatialdata import protocols


@pytest.fixture
def local_test_subject():
    yield LocalTestSubject
    spatialdata.executive.shutdown()


class LocalTestSubject(spatialdata.component):

    cs = protocols.coordinate_system()
