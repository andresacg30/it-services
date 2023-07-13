import pytest

from app.services.base_config import BaseService, BaseJob


class MockService(BaseService):
    def register_jobs(self) -> None:
        pass

    def process_job(self, job, file):
        pass

    def export_job(self):
        pass

    def get_jobs(self):
        pass


class MockJob(BaseJob):
    def process(self, file):
        pass

    def finish(self):
        pass


@pytest.fixture
def MockerService():
    return MockService


@pytest.fixture
def MockerJob():
    return MockJob
