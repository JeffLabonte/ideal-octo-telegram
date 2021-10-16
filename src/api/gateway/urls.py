from rest_framework.routers import SimpleRouter

from api.gateway.views import GatewayViewSet


router = SimpleRouter()

router.register("gateway", GatewayViewSet, basename="gateway")

urlpatterns = router.urls
