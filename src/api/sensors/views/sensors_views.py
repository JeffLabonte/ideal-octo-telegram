from rest_framework import mixins

from api.sensors.serializers import SensorsWriteSerializer
from common.views.common_viewset import CommonViewSet
from sensors.models import Sensors


class SensorsViewSet(
    mixins.CreateModelMixin,
    CommonViewSet,
):
    queryset = Sensors.objects.all()

    serializer_class = {
        "create": SensorsWriteSerializer,
    }
