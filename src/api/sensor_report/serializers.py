from rest_framework import serializers
from api.sensor.serializers import SensorGetSerializer
from api.sensor_target.serializers import SensorTargetGetSerializer

from sensor_report.models import SensorReport


class SensorReportGetSerializer(serializers.ModelField):
    id = serializers.UUIDField()
    sensor = SensorGetSerializer()
    target = SensorTargetGetSerializer()

    class Meta:
        model = SensorReport
        fields = [
            "id",
            "type",
            "value",
            "sensor",
            "target",
        ]
