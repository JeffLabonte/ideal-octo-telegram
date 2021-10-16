from rest_framework import serializers

from gateway.models import Gateway
from sensors.constants import TYPE_CHOICES
from sensors.models import Sensors


class SensorsWriteSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(
        choices=TYPE_CHOICES,
    )

    def create(self, validated_data):
        print(self.parent)
        return super().create(validated_data)

    class Meta:
        model = Sensors
        fields = ("type",)


class GatewayWriteSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=50,
    )
    sensors = SensorsWriteSerializer(many=True)

    class Meta:
        model = Gateway
        fields = (
            "name",
            "sensors",
        )
