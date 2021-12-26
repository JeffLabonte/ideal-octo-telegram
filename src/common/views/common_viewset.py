from rest_framework.generics import CreateAPIView
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class CommonViewSet(GenericViewSet):
    def get_serializer_class(self):
        if not (serializer_class := getattr(self, "serializer_class", {})):
            raise NotImplementedError("You need to implement `serializer_class` in your view")
        return serializer_class.get(self.action)
