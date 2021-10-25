from datetime import datetime

from rest_framework import serializers

from sensor.constants import TYPE_CHOICES
from sensor.models import Sensor


class SensorWriteSerializer(
    serializers.ModelSerializer,
):
    type = serializers.ChoiceField(
        choices=TYPE_CHOICES,
    )
    name = serializers.CharField(
        max_length=60,
        required=False,
        default=lambda: str(datetime.utcnow()),
    )

    class Meta:
        model = Sensor
        fields = (
            "type",
            "name",
        )


class SensorGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = (
            "id",
            "type",
            "name",
        )
