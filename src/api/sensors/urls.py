from rest_framework.routers import SimpleRouter

from api.sensors.views.devices_views import DeviceViewSet
from api.sensors.views.sensors_views import SensorsViewSet

router = SimpleRouter()
router.register("sensors", SensorsViewSet, basename="sensors")
router.register("devices", DeviceViewSet, basename="devices")

urlpatterns = router.urls
