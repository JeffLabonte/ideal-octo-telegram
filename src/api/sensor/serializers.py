from rest_framework import serializers
from api.gateway.serializers import GatewayWriteSerializer
from gateway.models import Gateway

from sensor.constants import TYPE_CHOICES


class SensorsWriteSerializer(
    serializers.ModelSerializer,
):
    type = serializers.ChoiceField(
        choices=TYPE_CHOICES,
    )
    gateway = GatewayWriteSerializer()

    class Meta:
        model = Gateway
        fields = (
            "type",
            "gateway",
        )
        default_fields = (
            "type",
            "gateway",
        )
