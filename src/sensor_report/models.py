import uuid

from django.db import models


class SensorData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    type = models.CharField(max_length=5)  # TODO Add Choices
