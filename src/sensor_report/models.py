import uuid

from django.db import models

from sensor_report.constants import SUPPORTED_TYPES


class SensorReport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    value_type = models.CharField(
        max_length=5,
        choices=SUPPORTED_TYPES,
    )
    value = models.CharField(
        max_length=20,
        blank=False,
        null=False,
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
