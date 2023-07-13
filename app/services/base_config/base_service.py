from abc import ABC, abstractmethod


class BaseService(ABC):
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
