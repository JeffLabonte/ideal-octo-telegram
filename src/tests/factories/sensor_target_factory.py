from factory import Factory
from factory.faker import Faker
from sensor_target.constants import SUPPORTED_TARGET_TYPE

from sensor_target.models import SensorTarget
from tests.factories.common import lazy_random_attribute


class SensorTargetFactory(Factory):
    id = Faker("uuid4")
    type = lazy_random_attribute(
        choices=list(SUPPORTED_TARGET_TYPE),
    )
    name = lazy_random_attribute(
        choices=[
            "Mushroom A",
            "Cannabis Indica Strain Plant",
            "Chives",
            "Garlic 1",
            "Garlic 3",
        ],
    )

    class Meta:
        model = SensorTarget
