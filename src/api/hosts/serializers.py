from hosts.models import Host
from api.hosts.validators import IPAddressValidator

from rest_framework import serializers


class HostGetSerializer(serializers.ModelSerializer):
    ip_address = serializers.CharField(
       validators=(
           IPAddressValidator(),
       ),
    )

    class Meta:
        model = Host
        fields = (
            "id",
            "ip_address",
            "host_credentials",
        )
