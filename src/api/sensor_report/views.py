from rest_framework.mixins import CreateModelMixin, ListModelMixin
from api.sensor_report.serializers import SensorReportGetSerializer, SensorReportWriteSerializer
from common.views.common_viewset import CommonViewSet
from sensor_report.models import SensorReport


class SensorReportViewSet(
    CreateModelMixin,
    ListModelMixin,
    CommonViewSet,
):
    queryset = SensorReport.objects.all()

    serializer_class = {
        "list": SensorReportGetSerializer,
        "create": SensorReportWriteSerializer,
    }
