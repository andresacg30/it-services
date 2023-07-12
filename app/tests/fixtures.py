import pytest

from app.services.base_service import BaseService


class MockService(BaseService):
    def process_job(self, job):
        pass

    def export_job(self, job):
        pass


@pytest.fixture
def MockerService():
    return MockService()
