import uuid

from django.db import models


class Host(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    ip_address = models.CharField(
        db_index=True,
        max_length=15,
    )
    use_ssh_key = models.BooleanField()
    ssh_key = models.TextField(
        max_length=2048,
        blank=False,
        null=False,
    )
    connection_information = models.ManyToManyField()
    password = models.CharField(
        max_length=200,
        blank=False,
        null=False
    )


class HostCredentials(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    is_ssh_key = models.BooleanField(
        default=False,
    )
    username = models.CharField()
    ssh_key = models.TextField(
        max_length=4096,
        null=True,
        blank=False
    )