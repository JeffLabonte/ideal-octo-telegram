from django.db.models.base import Model
from rest_framework import serializers


class UUIDPrimaryKeyRelatedField(serializers.UUIDField):
    """
    Allow you to write relations in a serializer that have a Model that uses a UUID as a priamry key
    """

    def __init__(self, model: Model, response_serializer: serializers.ModelSerializer, **kwargs):
        """
        Requires a Model
        """
        self.model = model
        self.response_serializer = response_serializer
        super().__init__(**kwargs)

    def to_internal_value(self, data: str) -> Model:
        uuid_pk = super().to_internal_value(data)
        return self.model.objects.get(pk=uuid_pk)

    def to_representation(self, value: Model) -> dict:
        return self.response_serializer(value).data
