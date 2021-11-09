from django.contrib import admin
from django.urls import path
from django.urls.conf import include


api_urls = [
    path("/", include("api.sensor.urls")),
    path("/", include("api.gateway.urls")),
    path("/", include("api.sensor_target.urls")),
    path("/", include("api.sensor_report.urls")),
]


urlpatterns = [
    path("admin", admin.site.urls),
    path("api", include(api_urls)),
    path("api/auth/", include("dj_rest_auth.urls")),
    path("api/auth/registration", include("dj_rest_auth.registration.urls")),
]
