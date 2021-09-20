from rest_framework import serializers

from common.serializers.default_ip_address import DefaultIpAddress
from sensors.models import Device, IpAddress, Sensors


class DeviceWriteSerializer(serializers.ModelSerializer):
    device_name = serializers.CharField(
        required=True,
    )

    ip_address = serializers.HiddenField(
        default=DefaultIpAddress,
    )

    def save(self, **kwargs):
        model = self.Meta.model

        ip_address = self.validated_data["ip_address"]
        query_args = {
            "device_name": self.validated_data["device_data"],
        }

        if model.objects.exists(**query_args) and ip_address in model.objects.get(
            **query_args
        ).ip_addresses.values_list("ip_address", flat=True):
            instance = model.objects.get(**query_args)
            instance.ip_addresses.add(ip_address)
            instance.save()
        else:
            super().save(**kwargs)

    class Meta:
        model = Device
        fields = ["id", "device_name"]


class SensorsWriteSerializer(serializers.ModelSerializer):
    sensor_data = serializers.JSONField(required=True)
    device_name = DeviceWriteSerializer(required=True)

    class Meta:
        model = Sensors
        fields = [
            "id",
            "sensor_data",
            "device_name",
        ]
