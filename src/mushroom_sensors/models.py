import uuid

from django.db import models


class Device(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    device_name = models.CharField(
        max_length=60,
        unique=True,
    )


class MushroomSensors(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    json_data = models.JSONField()
    device = models.ForeignKey(
        to=Device,
        default=None,
        null=True,
        on_delete=models.CASCADE,
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
    )
