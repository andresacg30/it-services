from abc import ABC, abstractmethod


class BaseService(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def process_job(self, *args, **kwargs):
        pass

    @abstractmethod
    def export_job(self, *args, **kwargs):
        pass
