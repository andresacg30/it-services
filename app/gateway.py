from fastapi import FastAPI, HTTPException

from app.services import register_services
from app.services.base_config import BaseService
from app.services.main import Factory
from app.utils.exceptions import InvalidServiceNameError, JobNotImplementedError

app = FastAPI()
factory = Factory()


def _get_service(service_name: str):
    try:
        service = factory.create_service_instance(
            service_name=service_name
        )
        return service()
    except InvalidServiceNameError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.on_event("startup")
async def register_app_services():
    register_services(factory=factory)


@app.post("/api/process-job")
async def process_job(service: str, job: str):
    if not service or not job:
        raise HTTPException(status_code=400, detail="No service or job provided")
    service_instance: BaseService = _get_service(service_name=service)
    try:
        service_instance.register_jobs()
        service_instance.process_job(job=job, file=job)
        file = service_instance.export_job()
        return {"job_type": job, "file": file}
    except JobNotImplementedError as e:
        raise HTTPException(status_code=400, detail=str(e))
