import uuid
from rest_framework import serializers
from api.sensor.serializers import SensorGetSerializer
from api.sensor_target.serializers import SensorTargetGetSerializer
from sensor_report.constants import SUPPORTED_TYPES

from sensor_report.models import SensorReport
from sensor_target.models import SensorTarget
from sensor.models import Sensor


class SensorReportGetSerializer(serializers.ModelField):
    id = serializers.UUIDField()
    sensor = SensorGetSerializer()
    target = SensorTargetGetSerializer()

    class Meta:
        model = SensorReport
        fields = [
            "id",
            "value_type",
            "value",
            "sensor",
            "target",
        ]


class SensorReportWriteSerializer(serializers.ModelField):
    id = serializers.HiddenField(
        default=uuid.uuid4(),
        partial=False,
    )
    value_type = serializers.ChoiceField(
        choices=SUPPORTED_TYPES,
        required=True,
    )
    value = serializers.CharField(
        max_length=20,
        required=True,
        allow_null=False,
    )
    sensor = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=Sensor.objects.all(),
    )
    target = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=SensorTarget.objects.all(),
    )

    class Meta:
        model = SensorReport
        fields = (
            "value_type",
            "value",
            "sensor",
            "target",
        )
