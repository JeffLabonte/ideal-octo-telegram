from rest_framework.mixins import CreateModelMixin, ListModelMixin
from api.sensor_report.serializers import SensorReportGetSerializer, SensorReportWriteSerializer
from common.views.common_viewset import CommonViewSet


class SensorReportViewSet(
    CreateModelMixin,
    ListModelMixin,
    CommonViewSet,
):
    serializer_class = {
        "list": SensorReportGetSerializer,
        "create": SensorReportWriteSerializer,
    }
