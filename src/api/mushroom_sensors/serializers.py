from rest_framework import serializers

from mushroom_sensors.models import MushroomSensors


class MushroomSensorsWriteSerializer(serializers.ModelSerializer):
    sensor_data = serializers.JSONField(required=True)

    class Meta:
        model = MushroomSensors
        fields = [

        ]
