from fastapi import HTTPException


def test__process_job__returns_not_found__when_invalid_job_type(client, mocker):
    mocker.patch(
        "app.gateway._get_service",
        side_effect=HTTPException(status_code=400, detail="Invalid job type"),
    )
    response = client.post("/api/process-job?job_type=None")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid job type"}
    assert response.headers["content-type"] == "application/json"
