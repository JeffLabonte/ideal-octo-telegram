from rest_framework.routers import SimpleRouter

from api.sensors.views.sensors_views import SensorsViewSet

router = SimpleRouter()
router.register("sensors", SensorsViewSet, basename="sensors")

urlpatterns = router.urls
