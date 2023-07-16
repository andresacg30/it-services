import pytest

from app.services import register_services
from app.services.main import Factory, ServiceConfigError, InvalidServiceNameError


def test__register_service__adds_service_to_services_dict(
    MockerService
):
    factory = Factory()
    factory.register(MockerService.name, MockerService)

    assert factory._services == {"mock": MockerService}
    assert factory._services["mock"] == MockerService


def test__register_service__raises_error_if_service_is_not_subclass_of_base_service():
    class DummyService:
        pass

    factory = Factory()

    with pytest.raises(ServiceConfigError) as e:
        factory.register("dummy", DummyService)
        assert str(e.value) == "Service must be a subclass of BaseService"

    assert factory._services == {}


def test__create_service_instance__returns_service_instance(
    MockerService
):
    factory = Factory()
    factory.register(MockerService.name, MockerService)

    service = factory.create_service_instance("mock")

    assert service == MockerService


def test__create_service_instance__raises_error_if_service_name_not_found():
    factory = Factory()

    with pytest.raises(InvalidServiceNameError) as e:
        factory.create_service_instance("not_found")
        assert str(e.value) == "Invalid service name"


def test__register_services__returns_added_services(
    mocker,
    MockerService
):
    factory = Factory()
    mocker.patch(
        "app.services.services_to_register",
        {"mock": MockerService}
    )
    services = register_services(factory=factory)

    assert services == {"mock": MockerService}
    assert services["mock"] == MockerService
