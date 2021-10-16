import uuid

from django.db import models

from sensor_report.constants import SUPPORTED_TYPES
from sensors.models import Sensors


class SensorData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    type = models.CharField(
        max_length=5,
        choices=SUPPORTED_TYPES,
    )
    value = models.CharField(
        max_length=20,
    )
    sensor = models.ForeignKey(
        Sensors,
        on_delete=models.CASCADE,
    )
