import uuid

from django.db import models

from sensor_target.constants import SUPPORTED_TARGET_TYPE


class SensorTarget(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    type = models.CharField(
        max_length=10,
        choices=SUPPORTED_TARGET_TYPE,
    )
    name = models.CharField(
        max_length=120,
        unique=True,
    )
