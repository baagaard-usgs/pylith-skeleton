# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2026 All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================

import pytest

import pyre

import pylith
from pylith import observers


@pytest.fixture
def load_yaml():
    cur_path = pyre.primitives.path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_solution_domain.yaml")


def test_traits_defaults():
    actor = observers.solution_domain()
    observer = actor()  # Component instance
    assert observer.__class__ == observers.OutputSolnDomain.OutputSolnDomain
    assert observer.output_basis_order == 1
    assert observer.refine_levels == 0


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    observer = test_subject.observer
    assert observer.__class__ == observers.OutputSolnDomain.OutputSolnDomain
    assert observer.output_basis_order == 0
    assert observer.refine_levels == 1


# End of file
