import uuid

from django.db import models


PROTOCOL_SUPPORTED = (
    (
        "ssh",
        "ssh",
    ),
)


class Credentials(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    username = models.CharField(
        max_length=160,
        blank=False,
    )
    password = models.CharField(
        max_length=160,
        blank=False,
    )


class Hosts(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    ip_address = models.CharField(
        blank=False,
        null=False,
        max_length=16,
    )
    port = models.IntegerField(
        blank=False,
    )
    protocol = models.CharField(
        choices=PROTOCOL_SUPPORTED,
        max_length=10,
    )

    credentials = models.ForeignKey(
        to=Credentials,
        on_delete=models.CASCADE,
        related_name="+",
    )

    class Meta:
        unique_together = (
            (
                "ip_address",
                "port",
                "protocol",
            ),
        )
