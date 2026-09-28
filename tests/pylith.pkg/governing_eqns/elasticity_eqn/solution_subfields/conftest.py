import pytest

import pylith
from pylith.protocols.governing_eqns.elasticity_eqn import solution_subfields


@pytest.fixture
def local_test_subject():
    yield LocalTestSubject
    pylith.reset()


class LocalTestSubject(pylith.component):

    solution = solution_subfields()
