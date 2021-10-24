from rest_framework import serializers
from api.sensor.serializers import SensorsWriteSerializer

from gateway.models import Gateway
from sensor.models import Sensor


class GatewayWriteSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(
        read_only=True,
    )
    name = serializers.CharField(
        max_length=50,
    )
    mac_address = serializers.CharField(
        max_length=17,
    )
    sensors = SensorsWriteSerializer(
        many=True,
    )

    def create(self, validated_data):
        sensors = validated_data.pop("sensors", [])
        gateway = Gateway.objects.create(**validated_data)
        for sensor in sensors:
            Sensor.objects.create(gateway=gateway, **sensor)
        return gateway

    class Meta:
        model = Gateway
        fields = (
            "id",
            "name",
            "mac_address",
            "sensors",
        )


class GatewayGetSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    mac_address = serializers.CharField()

    class Meta:
        model = Gateway
        fields = (
            "id",
            "name",
            "mac_address",
        )
