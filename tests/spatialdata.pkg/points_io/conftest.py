import pytest

import spatialdata
from spatialdata import protocols


@pytest.fixture
def local_test_subject():
    yield LocalTestSubject
    spatialdata.reset()


class LocalTestSubject(spatialdata.component):

    stations = protocols.points_io()
