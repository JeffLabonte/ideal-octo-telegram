from rest_framework.routers import SimpleRouter

from api.sensor_target.views import SensorTargetViewSet


router = SimpleRouter

router.register(
    "target",
    SensorTargetViewSet,
    basename="target",
)

urlpatterns = router.urls
