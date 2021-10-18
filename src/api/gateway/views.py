from rest_framework import mixins
from api.gateway.serializers import GatewayGetSerializer, GatewayWriteSerializer

from common.views.common_viewset import CommonViewSet
from gateway.models import Gateway


class GatewayViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    CommonViewSet,
):
    queryset = Gateway.objects.all()

    serializer_class = {
        "create": GatewayWriteSerializer,
        "list": GatewayGetSerializer,
        "retrieve": GatewayGetSerializer,
    }
