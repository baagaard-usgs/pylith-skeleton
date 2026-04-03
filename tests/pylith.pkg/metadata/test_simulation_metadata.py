import pathlib

import pytest

import pylith
from pylith import metadata


@pytest.fixture
def load_yaml():
    cur_path = pathlib.Path(__file__).parent
    pylith.loadConfiguration(cur_path / "test_simulation_metadata.yaml")


def test_traits_defaults():
    sim_metadata = metadata.simulation_metadata()  # Actor
    assert sim_metadata().__class__ == metadata.SimulationMetadata.SimulationMetadata
    assert sim_metadata.description is None
    assert sim_metadata.authors == []
    assert sim_metadata.keywords == []
    assert sim_metadata.features == []
    assert sim_metadata.arguments == []
    assert sim_metadata.base == []
    assert sim_metadata.version is None
    assert sim_metadata.pylith_version == []


def test_traits_yaml(load_yaml, local_test_subject):
    test_subject = local_test_subject(name="test_subject")
    sim_metadata = test_subject.metadata
    assert sim_metadata.__class__ == metadata.SimulationMetadata.SimulationMetadata
    assert sim_metadata.description == "Test run"
    assert sim_metadata.authors == ["Alice", "Bob"]
    assert sim_metadata.keywords == ["test", "pylith"]
    assert sim_metadata.features == ["feature1", "feature2"]
    assert sim_metadata.arguments == ["--verbose"]
    assert sim_metadata.base == ["base.yaml"]
    assert sim_metadata.version == "1.0"
    assert sim_metadata.pylith_version == [">=1.11"]
