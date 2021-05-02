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
        key_name="host_credentials_username"
    )
    password = EncryptedCharField(
        blank=False,
        null=False,
        max_length=256,
        key_name="host_credentials_password"
    )
    ssh_key = EncryptedTextField(
        max_length=4096,
        null=True,
        blank=False,
        key_name="host_credentials_ssh_keys"
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
    host_credentials = models.ManyToManyField(
        to=HostCredentials,
        related_name="+",
    )
