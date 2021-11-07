from rest_framework import serializers

from sensor_target.constants import SUPPORTED_TARGET_TYPE
from sensor_target.models import SensorTarget


class SensorTargetWriteSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(
        choices=SUPPORTED_TARGET_TYPE,
        blank=False,
    )

    class Meta:
        meta = SensorTarget
        fields = (
            "name",
            "type",
        )
