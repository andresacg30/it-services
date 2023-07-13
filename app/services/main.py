from app.utils.exceptions import InvalidServiceNameError, ServiceConfigError
from .base_config.base_service import BaseService


class Factory:
    def __init__(self):
        self._services = {}

    def register(self, service_name: str, service: BaseService) -> None:
        if not issubclass(service, BaseService):
            raise ServiceConfigError(
                "Service must be a subclass of BaseService"
            )
        self._services[service_name] = service

    def create_service_instance(self, service_name: str) -> BaseService:
        service = self._services.get(service_name)
        if not service:
            raise InvalidServiceNameError("Invalid service name")
        return service

    def get_services(self):
        return self._services
