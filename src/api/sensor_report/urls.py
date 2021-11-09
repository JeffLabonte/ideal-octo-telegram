from rest_framework.routers import SimpleRouter

from api.sensor_report.views import SensorReportViewSet


router = SimpleRouter()

router.register(
    "report",
    SensorReportViewSet,
    basename="report",
)

urlpatterns = router.urls
