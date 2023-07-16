from abc import ABC, abstractmethod
from fastapi import UploadFile


class BaseJob(ABC):
    name: str
    file: str

    @abstractmethod
    def process(self, file: UploadFile) -> None:
        pass

    @abstractmethod
    def finish(self):
        pass
