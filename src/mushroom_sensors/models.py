import uuid
from django.db import models


class MushroomSensors(models.Model):
    id = models.UUIDField(default=uuid.uuid4)
    json_data = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

