from rest_framework import mixins

from api.sensor.serializers import SensorGetSerializer, SensorWriteSerializer
from common.views.common_viewset import CommonViewSet


class SensorViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    CommonViewSet,
):
    serializer_class = {
        "create": SensorWriteSerializer,
        "retrieve": SensorGetSerializer,
        "update": SensorWriteSerializer,
    }
