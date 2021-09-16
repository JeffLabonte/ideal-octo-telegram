from rest_framework import serializers

from hosts.models import Credentials, Hosts


class HostsGetSerializer(serializers.ModelSerializer):
    ip_address = serializers.CharField()
    port = serializers.IntegerField()
    protocol = serializers.ChoiceField(choices=None)  # TODO Add Choices

    class Meta:
        model = Hosts
        fields = {
            "id",
            "ip_address",
            "port",
            "protocol",
        }
        default_fields = {"id", "ip_address", "port", "protocol"}


class CredentialsWriteSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = Credentials
        fields = {
            "username",
            "password",
        }
        default_fields = {
            "username",
            "password",
        }


class HostsWriteSerialzer(serializers.ModelSerializer):
    ip_address = serializers.CharField(
        required=True, validators=[]
    )  # TODO Add IP Address Validator
    port = serializers.IntegerField(
        required=True, validators=[]
    )  # TODO Limit to maximum port available
    protocol = serializers.ChoiceField(required=True, choices=None)  # TODO Add Choices

    credentials = CredentialsWriteSerializer(required=True)

    class Meta:
        model = Hosts
        fields = {
            "id",
            "ip_address",
            "port",
            "protocol",
            "credentials",
        }
        default_fields = {
            "id",
            "ip_address",
            "port",
            "protocol",
            "credentials",
        }
