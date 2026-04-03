import pathlib

import pytest

from pyre.units.length import meter

import pylith
from pylith import problems

# only import modules here?
from pylith.mesh_initializers import InitializerSerial;
from pylith.monitors import ProgressMonitorStep
from pylith.scales import QuasistaticElasticity
from pylith.governing_eqns.elasticity_eqn import ElasticityEqn


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_greens_fns.yaml")


def test_traits_defaults():
    problem = problems.greens_fns()  # Actor
    assert problem().__class__ == problems.GreensFns.GreensFns
    assert problem.initialize_only == False
    assert problem.scales().__class__ == QuasistaticElasticity.QuasistaticElasticity
    assert problem.mesh_initializer().__class__ == InitializerSerial.InitializerSerial
    assert problem.progress_monitor().__class__ == ProgressMonitorStep.ProgressMonitorStep
    assert problem.governing_eqn().__class__ == ElasticityEqn.ElasticityEqn


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    problem = test_subject.problem
    assert problem.__class__ == problems.GreensFns.GreensFns
    assert problem.initialize_only == False
    assert problem.scales.length_scale == 0.1*meter
    assert problem.mesh_initializer().__class__ == InitializerSerial.InitializerSerial
    assert problem.progress_monitor.update_percent == 10.0
    assert problem.governing_eqn().__class__ == ElasticityEqn.ElasticityEqn
