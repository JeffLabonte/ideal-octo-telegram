from factory import Factory
from factory.faker import Faker


class SensorTargetFactory(Factory):
    id = Faker("mac_address")
