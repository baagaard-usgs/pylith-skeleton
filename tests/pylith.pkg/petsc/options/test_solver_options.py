import pathlib

import pytest

import pylith
from pylith.petsc import options
from pylith.petsc.options import SolverOptions
from pylith.petsc.options import groups


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_solver_options.yaml")


def test_traits_defaults():
    actor = options.solver_options()
    options_manager = actor()  # Component instance
    assert options_manager.__class__ == SolverOptions.SolverOptions

    solver = options_manager.solver
    assert solver.__class__ == groups.GroupList.GroupList
    assert solver.enabled == False
    assert solver.options == []

    initial_guess = options_manager.initial_guess
    assert initial_guess.__class__ == groups.GroupList.GroupList
    assert initial_guess.enabled == False
    assert initial_guess.options == []

    tolerances = options_manager.tolerances
    assert tolerances.__class__ == groups.GroupList.GroupList
    assert tolerances.enabled == False
    assert tolerances.options == []

    adaptive_ts = options_manager.adaptive_ts
    assert adaptive_ts.__class__ == groups.GroupList.GroupList
    assert adaptive_ts.enabled == False
    assert adaptive_ts.options == []

    monitoring = options_manager.monitoring
    assert monitoring.__class__ == groups.GroupList.GroupList
    assert monitoring.enabled == False
    assert monitoring.options == []


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    options_manager = test_subject.options_manager
    assert options_manager.__class__ == SolverOptions.SolverOptions

    solver = options_manager.solver
    assert solver.__class__ == groups.GroupList.GroupList
    assert solver.enabled == True
    assert solver.options == [
        ("ts_type", "beuler"),
        ("pc_type", "gamg"),
        ("pc_gamg_coarse_eq_limit", "200"),
        ("mg_fine_ksp_max_it", "5"),
    ]

    initial_guess = options_manager.initial_guess
    assert initial_guess.__class__ == groups.GroupList.GroupList
    assert initial_guess.enabled == False
    assert initial_guess.options == [
        ("ksp_guess_type", "pod"),
        ("ksp_guess_pod_size", "8"),
    ]

    tolerances = options_manager.tolerances
    assert tolerances.__class__ == groups.GroupList.GroupList
    assert tolerances.enabled == True
    assert tolerances.options == [
        ("ksp_rtol", "1.0e-12"),
        ("ksp_atol", "1.0e-7"),
        ("snes_rtol", "5.0e-6"),
        ("snes_atol", "5.0e-2"),
    ]

    adaptive_ts = options_manager.adaptive_ts
    assert adaptive_ts.__class__ == groups.GroupList.GroupList
    assert adaptive_ts.enabled == True
    assert adaptive_ts.options == [
        ("ts_adapt_type", "basic"),
        ("ts_adapt_safety", "0.2"),
        ("ts_adapt_reject_safety", "0.1"),
        ("ts_atol", "0.05"),
        ("ts_rtol", "0.05"),
        ("ts_adapt_monitor", "true"),
    ]

    monitoring = options_manager.monitoring
    assert monitoring.__class__ == groups.GroupList.GroupList
    assert monitoring.enabled == True
    assert monitoring.options == [
        ("ts_monitor",),
        ("ksp_monitor",),
        ("snes_monitor",),
        ("ksp_converged_reason",),
        ("snes_converged_reason",),
        ("ts_error_if_step_fails",),
        ("ksp_error_if_not_converged",),
        ("snes_error_if_not_converged",),
    ]
