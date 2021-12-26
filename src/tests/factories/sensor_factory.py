import factory
from factory.faker import Faker

from sensor.constants import TYPE_CHOICES
from sensor.models import Sensor
from tests.factories.common import lazy_random_attribute
from tests.factories.gateway_factory import GatewayFactory


class SensorFactory(factory.Factory):
    id = Faker("uuid4")
    name = Faker("domain_name")
    type = lazy_random_attribute(choices=list(TYPE_CHOICES))
    gateway = factory.SubFactory(GatewayFactory)

    class Meta:
        model = Sensor
