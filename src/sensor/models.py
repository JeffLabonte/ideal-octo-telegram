import uuid

from django.db import models

from common.models.mixins.timestamps import TimeStampMixin
from sensors.constants import TYPE_CHOICES


class IpAddress(
    TimeStampMixin,
    models.Model,
):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    gateway = models.ForeignKey(
        to="gateway.Gateway",
        on_delete=models.CASCADE,
    )
    ip_address = models.CharField(
        max_length=15,
    )


class Sensor(
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
    gateway = models.ForeignKey(
        to="gateway.Gateway",
        default=None,
        null=True,
        on_delete=models.CASCADE,
    )
