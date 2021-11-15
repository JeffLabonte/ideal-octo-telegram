from rest_framework import mixins

from api.sensor_target.serializers import SensorTargetGetSerializer, SensorTargetWriteSerializer
from common.views.common_viewset import CommonViewSet
from sensor_target.models import SensorTarget


class SensorTargetViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    CommonViewSet,
):
    queryset = SensorTarget.objects.all()

    serializer_class = {
        "list": SensorTargetGetSerializer,
        "retrieve": SensorTargetGetSerializer,
        "create": SensorTargetWriteSerializer,
    }
