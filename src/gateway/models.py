import uuid

from django.db import models

from common.models.mixins.timestamps import TimeStampMixin


class Gateway(TimeStampMixin, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50, unique=True, required=True)
