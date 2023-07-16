import pytest

from app.services.base_config import BaseService, BaseJob


class MockService(BaseService):
    name = "mock"
    finished_file = None
    jobs_to_register = {}

    def register_jobs(self):
        pass

    def process_job(self, job, file):
        pass

    def export_job(self):
        pass

    def get_jobs(self):
        pass


class MockJob(BaseJob):
    name = "mock_job"
    file = None

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
