from django.db import transaction
from rest_framework import serializers
from api.sensor.serializers import SensorGetSerializer, SensorWriteSerializer

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
    sensors = SensorWriteSerializer(
        many=True,
        write_only=True,
        required=False,
    )
    gateway_sensors = SensorGetSerializer(
        many=True,
        read_only=True,
    )

    @transaction.atomic
    def create(self, validated_data):
        sensors = validated_data.pop("sensors", [])
        gateway = Gateway.objects.create(**validated_data)
        sensors = [Sensor(gateway=gateway, **sensor) for sensor in sensors]
        Sensor.objects.bulk_create(sensors)

        return gateway

    class Meta:
        model = Gateway
        fields = (
            "id",
            "name",
            "mac_address",
            "sensors",
            "gateway_sensors",
        )


class GatewayGetSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    mac_address = serializers.CharField()
    sensors = SensorGetSerializer(
        many=True,
        source="gateway_sensors",
    )

    class Meta:
        model = Gateway
        fields = (
            "id",
            "name",
            "mac_address",
            "sensors",
        )
