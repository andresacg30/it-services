from .base_service.base_service import BaseService


class Factory:
    def __init__(self):
        self._services = {}

    def register(self, service_name: str, service: BaseService) -> None:
        if not issubclass(service, BaseService):
            raise ValueError("Service must be a subclass of BaseService")
        self._services[service_name] = service

    def create_service_instance(self, service_name: str) -> BaseService:
        service = self._services.get(service_name)
        if not service:
            raise ValueError("Invalid service name")
        return service
