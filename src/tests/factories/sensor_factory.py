from factory import Factory
from factory.declarations import LazyAttribute
from factory.faker import Faker
from sensor.constants import TYPE_CHOICES

from sensor.models import Sensor
from tests.factories.common import lazy_random_attribute
from tests.factories.gateway_factory import GatewayFactory


class SensorFactory(Factory):
    id = Faker("uuid4")
    name = Faker("domain_name")
    type = lazy_random_attribute(choices=TYPE_CHOICES)
    gateway = LazyAttribute(lambda: GatewayFactory.create())

    class Meta:
        model = Sensor
