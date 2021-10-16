import uuid

from django.db import models

from sensor_report.constants import SUPPORTED_TYPES


class SensorData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    type = models.CharField(
        max_length=5,
        choices=SUPPORTED_TYPES,
    )
    value = models.CharField(
        max_length=20,
    )
