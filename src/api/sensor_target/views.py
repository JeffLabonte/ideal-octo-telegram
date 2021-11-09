from rest_framework import mixins

from api.sensor_target.serializers import SensorTargetGetSerializer, SensorTargetWriteSerializer
from common.views.common_viewset import CommonViewSet


class SensorTargetViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    CommonViewSet,
):
    serializer_class = {
        "list": SensorTargetGetSerializer,
        "retrieve": SensorTargetGetSerializer,
        "create": SensorTargetWriteSerializer,
    }
