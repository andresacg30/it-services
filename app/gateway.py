from fastapi import FastAPI, HTTPException

from app.services.main import Factory

app = FastAPI()
factory = Factory()


def _get_service(service_name: str):
    service = factory.create_service_instance(
        service_name=service_name
    )
    return service


@app.post("/api/process-job")
async def process_job(job_type: str):
    if job_type:
        service = _get_service(job_type)
        service.process_job()
        file = service.export_job()
        return {"job_type": job_type, "file": file}
    else:
        raise HTTPException(status_code=400, detail="No job type provided")
