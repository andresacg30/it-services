import pytest
import tempfile

from fastapi import UploadFile

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


@pytest.fixture
def mocker_file():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        yield f


@pytest.fixture
def mocker_pdf_file(mocker, mocker_file):
    mocker_pdf_file = mocker.create_autospec(UploadFile)
    mocker_pdf_file.filename = "mock_file.pdf"
    mocker_pdf_file.file = mocker_file
    return mocker_pdf_file


@pytest.fixture
def mocker_docx_file(mocker):
    mocker_docx_file = mocker.create_autospec(UploadFile)
    mocker_docx_file.filename = "./app/mock_file.docx"
    return mocker_docx_file
