import uuid

from django.db import models

from commons.models.fields import EncryptedCharField, EncryptedTextField


class HostCredentials(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    is_ssh_key = models.BooleanField(
        default=False,
    )
    username = EncryptedCharField(
        blank=False,
        null=False,
        max_length=64,
    )
    password = EncryptedCharField(
        blank=False,
        null=False,
        max_length=256,
    )
    ssh_key = EncryptedTextField(
        max_length=4096,
        null=True,
        blank=False
    )


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
    host_credentials = models.ManyToManyField(
        to=HostCredentials,
        related_name="+",
        null=False,
    )
