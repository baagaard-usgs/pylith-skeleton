import pathlib

import pytest

import pylith
from pylith import monitors


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_progress_monitor_step.yaml")


def test_traits_defaults():
    monitor = monitors.progress_monitor_step()  # Actor
    assert monitor().__class__ == monitors.ProgressMonitorStep.ProgressMonitorStep
    assert monitor.uri is None
    assert monitor.update_percent == 5.0


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    monitor = test_subject.monitor
    assert monitor.__class__ == monitors.ProgressMonitorStep.ProgressMonitorStep
    assert str(monitor.uri) == "progress.txt"
    assert monitor.update_percent == 10.0
