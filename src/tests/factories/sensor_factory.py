import random
from factory import Factory
from factory.declarations import LazyAttribute
from factory.faker import Faker
from sensor.constants import TYPE_CHOICES

from sensor.models import Sensor
from tests.factories.gateway_factory import GatewayFactory


def lazy_random_attribute(choices: list) -> LazyAttribute:
    def get_random_choice(*args, **kwargs):
        choices_length = len(choices)
        return choices[random.randint(0, choices_length - 1)]

    return LazyAttribute(get_random_choice)


class SensorFactory(Factory):
    id = Faker("uuid4")
    name = Faker("domain_name")
    type = lazy_random_attribute(choices=TYPE_CHOICES)
    gateway = LazyAttribute(lambda: GatewayFactory.create())

    class Meta:
        model = Sensor
