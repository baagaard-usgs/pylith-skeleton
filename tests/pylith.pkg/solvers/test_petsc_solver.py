# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2026 All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================

import pathlib

import pytest

import pylith
from pylith import solvers


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_petsc_solver.yaml")


def test_traits_defaults():
    actor = solvers.petsc()
    solver = actor()  # Component instance
    assert solver.__class__ == solvers.SolverPetsc.SolverPetsc
    assert solver.formulation == "implicit"


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    solver = test_subject.solver
    assert solver.__class__ == solvers.SolverPetsc.SolverPetsc
    assert solver.formulation == "explicit"


# End of file
