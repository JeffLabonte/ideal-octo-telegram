import itertools
from rest_framework import serializers

from sensors.models import Device, IpAddress, Sensors


class DeviceWriteSerializer(serializers.ModelSerializer):
    device_name = serializers.CharField(
        required=True,
    )

    def _get_ip_from_context(self) -> str:
        return self.context.get("request").META.get("REMOTE_ADDR")

    def create(self, validated_data):
        instance = self.Meta.model.objects.get_or_create(**validated_data)[0]
        ip_address = IpAddress(
            ip_address=self._get_ip_from_context(),
            device=instance,
        )
        ip_address.save()
        return instance

    class Meta:
        model = Device
        fields = ("device_name",)


class SensorsWriteSerializer(serializers.ModelSerializer):
    sensors_data = serializers.JSONField(required=True)
    device = DeviceWriteSerializer(required=True)

    def create(self, validated_data):
        device_instance = self.fields["device"].create(
            validated_data=validated_data.pop("device"),
        )
        instance = super().create(validated_data=validated_data)
        instance.device = device_instance
        instance.save()
        return instance

    class Meta:
        model = Sensors
        fields = [
            "sensors_data",
            "device",
        ]
