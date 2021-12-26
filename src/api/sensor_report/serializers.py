import uuid

from rest_framework import serializers
from api.sensor.serializers import SensorGetSerializer
from api.sensor_target.serializers import SensorTargetGetSerializer
from common.serializers.uuid_primary_key_related_field import UUIDPrimaryKeyRelatedField
from sensor_report.constants import SUPPORTED_TYPES

from sensor_report.models import SensorReport
from sensor_target.models import SensorTarget
from sensor.models import Sensor


class SensorReportGetSerializer(serializers.ModelSerializer):
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


class SensorReportWriteSerializer(serializers.ModelSerializer):
    id = serializers.HiddenField(
        default=uuid.uuid4,
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
    sensor = UUIDPrimaryKeyRelatedField(
        model=Sensor,
        response_serializer=SensorGetSerializer,
        required=True,
        write_only=True,
    )
    target = UUIDPrimaryKeyRelatedField(
        model=SensorTarget,
        response_serializer=SensorTargetGetSerializer,
        required=True,
        write_only=True,
    )

    class Meta:
        model = SensorReport
        fields = (
            "id",
            "value_type",
            "value",
            "sensor",
            "target",
        )
