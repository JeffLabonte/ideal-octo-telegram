from contextlib import contextmanager

import pytest
from django.urls.base import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APIClient

from sensor.models import Sensor


@contextmanager
def create_sensors():
    sensors = [
        Sensor.objects.create(
            name="Humidity",
            type="humidity",
        ),
        Sensor.objects.create(
            name="Temperature",
            type="temperature",
        ),
    ]
    yield sensors
    Sensor.objects.filter(
        pk__in=[sensor.pk for sensor in sensors],
    ).delete()


@pytest.mark.django_db
def test__sensor_viewset__list_should_return_multiple_sensors(
    auth_client: APIClient,
):
    with create_sensors() as sensors:
        url = reverse("sensor-list")
        response = auth_client.get(
            path=url,
        )

        assert response.status_code == HTTP_200_OK

        response_json = response.json()
        assert len(response_json) == len(sensors)
