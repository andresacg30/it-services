def test__process_job__returns_400_error__when_no_service_is_provided(
    client
):
    response = client.post("/api/process-job?service=&job=test")

    assert response.status_code == 400
    assert response.json() == {"detail": "No service or job provided"}
    assert response.headers["content-type"] == "application/json"


def test__process_job__returns_400_error__when_no_job_is_provided(
    client,
    mocker
):
    mocker.patch("app.gateway.factory.create_service_instance")
    response = client.post("/api/process-job?service=test&job=")

    assert response.status_code == 400
    assert response.json() == {"detail": "No service or job provided"}
    assert response.headers["content-type"] == "application/json"


def test__process_job__returns_400_error__when_no_service_nor_job_is_provided(
    client
):
    response = client.post("/api/process-job?service=&job=")

    assert response.status_code == 400
    assert response.json() == {"detail": "No service or job provided"}
    assert response.headers["content-type"] == "application/json"


def test__process_job__returns_400_error__when_service_not_found(
    client,
):

    response = client.post("/api/process-job?service=not_found&job=test")

    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid service name"}
    assert response.headers["content-type"] == "application/json"


def test__process_job__returns_file__when_job_type_found(
    client,
    mocker,
    MockerService
):
    service = mocker.create_autospec(MockerService)

    service.process_job.return_value = None
    service.export_job.return_value = "mock_file"
    mocker.patch(
        "app.gateway._get_service",
        return_value=service
    )

    response = client.post("/api/process-job?service=mock&job=mock")

    service.process_job.assert_called_once()
    service.export_job.assert_called_once()
    assert response.status_code == 200
    assert response.json() == {"job_type": "mock", "file": "mock_file"}
