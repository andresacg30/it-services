import pytest
from fastapi.testclient import TestClient

from app.gateway import app
from .fixtures import *  # noqa: F401, F403

@pytest.fixture
def client():
    return TestClient(app)
