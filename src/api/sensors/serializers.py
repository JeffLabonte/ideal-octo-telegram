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
        instance = self.Meta.model.objects.create(**validated_data)
        ip_address = IpAddress(
            ip_address=self._get_ip_from_context(),
        )
        ip_address.save()
        instance.ip_addresses.set([ip_address])
        return instance

    def update(self, instance, validated_data):
        ip_addresses = set(
            itertools.chain(
                instance.ip_addresses.all(),
                [
                    self._get_ip_from_context(),
                ],
            )
        )
        instance.ip_addresses.set(ip_addresses)
        return super().update(instance, validated_data)

    class Meta:
        model = Device
        fields = ("device_name",)


class SensorsWriteSerializer(serializers.ModelSerializer):
    sensor_data = serializers.JSONField(required=True)
    device_name = DeviceWriteSerializer(required=True)

    class Meta:
        model = Sensors
        fields = [
            "sensor_data",
            "device_name",
        ]
