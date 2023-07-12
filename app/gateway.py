from fastapi import FastAPI, HTTPException

from app.services.main import Factory, InvalidServiceNameError

app = FastAPI()
factory = Factory()


def _get_service(service_name: str):
    try:
        service = factory.create_service_instance(
            service_name=service_name
        )
        return service
    except InvalidServiceNameError:
        raise HTTPException(status_code=400, detail="Invalid service name")


@app.post("/api/process-job")
async def process_job(service: str, job: str):
    if not service or not job:
        raise HTTPException(status_code=400, detail="No service or job provided")
    service = _get_service(service_name=service)
    service.process_job(job=job)
    file = service.export_job()
    return {"job_type": job, "file": file}
