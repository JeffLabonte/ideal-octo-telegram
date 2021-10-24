from rest_framework import serializers

from sensor.constants import TYPE_CHOICES
from sensor.models import Sensor


class SensorWriteSerializer(
    serializers.ModelSerializer,
):
    type = serializers.ChoiceField(
        choices=TYPE_CHOICES,
    )

    class Meta:
        model = Sensor
        fields = ("type",)


class SensorGetSerializer(serializers.ModelSerializer):
    type = serializers.CharField()

    class Meta:
        model = Sensor
        fields = (
            "id",
            "type",
        )
