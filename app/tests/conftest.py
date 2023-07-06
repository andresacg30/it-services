import pytest
from fastapi.testclient import TestClient

from app.gateway import app

@pytest.fixture
def client():
    return TestClient(app)