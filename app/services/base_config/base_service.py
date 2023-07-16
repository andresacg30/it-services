from abc import ABC, abstractmethod
from fastapi import UploadFile


class BaseService(ABC):
    name: str
    finished_file: UploadFile
    jobs_to_register: dict

    @abstractmethod
    def register_jobs(self) -> None:
        pass

    @abstractmethod
    def process_job(self, job: str, file: bytes) -> None:
        pass

    @abstractmethod
    def export_job(self) -> bytes:
        pass

    @abstractmethod
    def get_jobs(self) -> dict:
        pass

    @abstractmethod
    def clean_up(self) -> None:
        pass
