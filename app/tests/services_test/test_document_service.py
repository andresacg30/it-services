import pytest

from app.services import DocumentService
from app.utils.exceptions import JobNotImplementedError


def test__register_jobs__adds_jobs_to_jobs_attribute():
    service = DocumentService()
    jobs_to_register = {"mock_job": "mock_job"}
    service.jobs_to_register = jobs_to_register
    service.register_jobs()
    assert service._jobs == jobs_to_register


def test__process_job__returns_file__when_job_type_found(
    mocker,
    MockerJob
):
    mock_job = mocker.create_autospec(MockerJob)
    instance_mock = mock_job.return_value
    instance_mock.process.return_value = None
    instance_mock.finish.return_value = "mock_file"
    service = DocumentService()
    service._jobs = {MockerJob.name: mock_job}

    service.process_job(job="mock_job", file="mock_file")

    instance_mock.process.assert_called_once_with(file="mock_file")
    instance_mock.finish.assert_called_once()


def test__process_job__raises_error__when_job_type_not_found(
    mocker,
    MockerJob
):
    dummy_job = mocker.create_autospec(MockerJob)
    service = DocumentService()

    with pytest.raises(JobNotImplementedError) as e:
        service.process_job(job=dummy_job, file="mock_file")
        assert str(e.value) == "Job not implemented"

    assert dummy_job.process.call_count == 0
    assert dummy_job.finish.call_count == 0
    assert service._jobs == {}
