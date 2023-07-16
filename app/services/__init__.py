import typing

from .main import Factory
# List services here
from .document_service.document_service import DocumentService


services_to_register = {
    DocumentService.name: DocumentService,
}


def register_services(factory: Factory) -> typing.List[typing.Dict]:
    for name, service in services_to_register.items():
        factory.register(service_name=name, service=service)
    return factory.get_services()
