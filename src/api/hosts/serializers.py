from hosts.models import Host

from rest_framework import serializers


class HostGetSerializer(serializers.ModelSerializer):
  ip_address = serializers.CharField()


  class Meta:
    model = Host
    fields = (
        "id",
        "ip_address",
        "host_credentials",
    )

