import pytest

import pylith
from pylith.protocols.governing_eqns.elasticity_eqn import bulk_rheology


@pytest.fixture
def local_test_subject():
    yield LocalTestSubject
    pylith.reset()


class LocalTestSubject(pylith.component):

    material = bulk_rheology()
