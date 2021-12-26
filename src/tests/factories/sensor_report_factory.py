from random import randint

import factory
from factory.base import Factory
from factory.faker import Faker
from sensor_report.constants import SUPPORTED_TYPES

from sensor_report.models import SensorReport
from tests.factories.common import lazy_random_attribute
from tests.factories.sensor_factory import SensorFactory
from tests.factories.sensor_target_factory import SensorTargetFactory


class SensorReportFactory(Factory):
    id = Faker("uuid4")
    value_type = lazy_random_attribute(
        choices=list(SUPPORTED_TYPES),
    )
    value = str(randint(0, 99999))
    sensor = factory.SubFactory(SensorFactory)
    target = factory.SubFactory(SensorTargetFactory)

    class Meta:
        model = SensorReport
