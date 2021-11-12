import uuid

from django.db import models

from sensor_report.constants import SUPPORTED_TYPES


class SensorTarget(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    type = models.CharField(
        max_length=5,
        choices=SUPPORTED_TYPES,
    )
    value = models.CharField(
        max_length=20,
    )
    sensor = models.ForeignKey(
        "sensor.Sensor",
        on_delete=models.CASCADE,
    )
    target = models.ForeignKey(
        "sensor_target.SensorTarget",
        on_delete=models.CASCADE,
        null=True,
    )
