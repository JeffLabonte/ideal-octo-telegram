from rest_framework import serializers

from mushroom_sensors.models import MushroomSensors


class DeviceWriteSerializer(serializers.ModelSerializer):
    pass


class MushroomSensorsWriteSerializer(serializers.ModelSerializer):
    sensor_data = serializers.JSONField(required=True)
    device_name = serializers.CharField(required=True)

    class Meta:
        model = MushroomSensors
        fields = []
