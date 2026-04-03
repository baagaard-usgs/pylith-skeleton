import pathlib

import pytest

import pylith
from pylith import solvers


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_petsc_solver.yaml")


def test_traits_defaults():
    solver = solvers.petsc()  # Actor
    assert solver().__class__ == solvers.SolverPetsc.SolverPetsc
    assert solver.formulation == "implicit"


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    solver = test_subject.solver
    assert solver.__class__ == solvers.SolverPetsc.SolverPetsc
    assert solver.formulation == "explicit"
