from app.services.base_config import BaseService, BaseJob
from app.utils.exceptions import JobNotImplementedError
from .jobs.pdf_to_word import PDFToWordJob


class DocumentService(BaseService):
    finished_file = None
    jobs_to_register = {
        "pdf-to-word": PDFToWordJob
    }

    def __init__(self):
        self._jobs = {}

    def register_jobs(self) -> None:
        for job_name, job in self.jobs_to_register.items():
            self._jobs[job_name] = job

    def process_job(self, job, file):
        if job not in self._jobs.keys():
            raise JobNotImplementedError("Job not implemented")
        selected_job: BaseJob = self._jobs.get(job)
        selected_job = selected_job()
        selected_job.process(file=file)
        self.finished_file = selected_job.finish()

    def export_job(self):
        return self.finished_file

    def get_jobs(self):
        return self._jobs
