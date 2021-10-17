from rest_framework import serializers

from gateway.models import Gateway


class GatewayWriteSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=50,
    )
    mac_address = serializers.CharField(
        max_length=17,
    )

    class Meta:
        model = Gateway
        fields = (
            "name",
            "mac_address",
        )
