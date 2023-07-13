from abc import ABC, abstractmethod


class BaseJob(ABC):

    @abstractmethod
    def process(self, file) -> None:
        pass

    @abstractmethod
    def finish(self):
        pass
