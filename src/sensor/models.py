import uuid

from django.db import models

from common.models.mixins.timestamps import TimeStampMixin
from sensor.constants import TYPE_CHOICES


class Sensor(
    TimeStampMixin,
    models.Model,
):
    # TODO Add model/part number of the sensor: cross-referent to digi-key/Amazon
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    name = models.CharField(
        max_length=60,
        blank=False,
        null=False,
        unique=True,
    )
    type = models.CharField(
        max_length=30,
        choices=TYPE_CHOICES,
    )
    gateway = models.ForeignKey(
        to="gateway.Gateway",
        default=None,
        null=True,
        on_delete=models.CASCADE,
        related_name="gateway_sensors",
    )
