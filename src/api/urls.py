from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("admin", admin.site.urls),
    path("api/", include("api.sensors.urls")),
    path("api/auth/", include("dj_rest_auth.urls")),
    path("api/auth/registration", include("dj_rest_auth.registration.urls")),
]
