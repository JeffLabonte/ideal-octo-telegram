from factory.base import Factory

from sensor_report.models import SensorReport


class SensorReportFactory(Factory):
    class Meta:
        model = SensorReport
