import uuid

from django.db import models

from common.models.mixins.timestamps import TimeStampMixin
from sensors.constants import TYPE_CHOICES


class Device(
    TimeStampMixin,
    models.Model,
):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    device_name = models.CharField(
        max_length=60,
        unique=True,
    )


class IpAddress(
    TimeStampMixin,
    models.Model,
):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    device = models.ForeignKey(
        to=Device,
        on_delete=models.CASCADE,
    )
    ip_address = models.CharField(
        max_length=15,
    )


class Sensors(
    TimeStampMixin,
    models.Model,
):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    type = models.CharField(
        max_length=30,
        choices=TYPE_CHOICES,
    )
    sensors_data = models.JSONField()
    device = models.ForeignKey(
        to=Device,
        default=None,
        null=True,
        on_delete=models.CASCADE,
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
    )
