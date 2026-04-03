import pathlib

import pytest

from pyre.units.time import year

import pylith
from pylith import monitors


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_progress_monitor_time.yaml")


def test_traits_defaults():
    monitor = monitors.progress_monitor_time()  # Actor
    assert monitor().__class__ == monitors.ProgressMonitorTime.ProgressMonitorTime
    assert monitor.uri is None
    assert monitor.update_percent == 5.0
    assert monitor.time_units == 1.0 * year


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    monitor = test_subject.monitor
    assert monitor.__class__ == monitors.ProgressMonitorTime.ProgressMonitorTime
    assert str(monitor.uri) == "progress_time.txt"
    assert monitor.update_percent == 2.0
    assert monitor.time_units == 0.5 * year
