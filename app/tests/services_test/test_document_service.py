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


def test__export_job__returns_file__temp_file__when_class_instance_has_finished_file(
    mocker_file
):
    service = DocumentService()
    service.finished_file = mocker_file.name

    response = service.export_job()

    assert response.split("/")[:-1] == mocker_file.name.split("/")[:-1]  # Exluding the file name


def test__export_job__returns_none__when_class_instance_has_no_finished_file(
):
    service = DocumentService()
    service.finished_file = None

    with pytest.raises(FileNotFoundError) as e:
        service.export_job()
        assert str(e.value) == "No file to export"


def test__clean_up__removes_file__when_class_instance_has_finished_file(
    mocker,
    mocker_file
):
    service = DocumentService()
    service.finished_file = mocker_file.name
    mocker.patch("os.remove")

    service.clean_up()

    assert service.finished_file is None
