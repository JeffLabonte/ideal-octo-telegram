from rest_framework import serializers
from gateway.models import Gateway

from sensors.models import IpAddress, Sensors


class GatewayWriteSerializer(serializers.ModelSerializer):
    device_name = serializers.CharField(
        required=True,
        source="name"
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
        model = Gateway
        fields = ("device_name",)


class SensorsWriteSerializer(serializers.ModelSerializer):
    sensors_data = serializers.JSONField(required=True)
    gateway = GatewayWriteSerializer(required=True)

    def create(self, validated_data):
        gateway_instance = self.fields["gateway"].create(
            validated_data=validated_data.pop("device"),
        )
        instance = super().create(validated_data=validated_data)
        instance.device = gateway_instance
        instance.save()
        return instance

    class Meta:
        model = Sensors
        fields = [
            "sensors_data",
            "device",
        ]
