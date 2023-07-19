import tempfile
import os

from fastapi import UploadFile

from app.services.base_config import BaseService, BaseJob
from app.utils.exceptions import JobNotImplementedError
from .jobs.pdf_to_word import PDFToWordJob


class DocumentService(BaseService):
    name = "document"
    finished_file: str
    jobs_to_register = {
        PDFToWordJob.name: PDFToWordJob
    }

    def __init__(self) -> None:
        self._jobs = {}

    def register_jobs(self) -> None:
        for job_name, job in self.jobs_to_register.items():
            self._jobs[job_name] = job

    def process_job(self, job: str, file: UploadFile) -> None:
        if job not in self._jobs.keys():
            raise JobNotImplementedError("Job not implemented")
        selected_job: BaseJob = self._jobs.get(job)
        selected_job = selected_job()
        selected_job.process(file=file)
        self.finished_file = selected_job.finish()

    def export_job(self) -> str:
        if not self.finished_file:
            raise FileNotFoundError("No file to export")
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            with open(self.finished_file, "rb") as f:
                temp_file.write(f.read())
            return temp_file.name

    def get_jobs(self) -> dict:
        return self._jobs

    def clean_up(self) -> None:
        if self.finished_file:
            self.finished_file = None
            os.remove(self.finished_file)
