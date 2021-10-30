from rest_framework import mixins

from api.sensor.serializers import SensorGetSerializer, SensorWriteSerializer
from common.views.common_viewset import CommonViewSet
from sensor.models import Sensor


class SensorViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    CommonViewSet,
):
    queryset = Sensor.objects.all()

    serializer_class = {
        "create": SensorWriteSerializer,
        "list": SensorGetSerializer,
        "update": SensorWriteSerializer,
    }
