from rest_framework.routers import SimpleRouter

from api.sensor.views import SensorViewSet

router = SimpleRouter()

router.register(
    "sensor",
    SensorViewSet,
    basename="sensor",
)

urlpatterns = router.urls
