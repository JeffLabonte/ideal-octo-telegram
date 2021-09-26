from rest_framework import mixins

from api.sensors.serializers import DeviceWriteSerializer
from common.views.common_viewset import CommonViewSet
from sensors.models import Device


class DeviceViewSet(
    mixins.CreateModelMixin,
    CommonViewSet,
):
    queryset = Device.objects.all()

    serializer_class = {
        "create": DeviceWriteSerializer,
    }
