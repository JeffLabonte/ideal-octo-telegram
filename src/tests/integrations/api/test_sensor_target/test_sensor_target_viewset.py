from django.urls.base import reverse
import pytest
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APIClient

from tests.factories.sensor_target_factory import SensorTargetFactory


def setup():
    return SensorTargetFactory.create_batch(size=3)


@pytest.mark.django_db
def test__sensor_target_viewset__list_sensor_target(
    auth_client: APIClient,
):
    sensor_targets = setup()
    url = reverse("target-list")

    response = auth_client.get(
        path=url,
    )

    assert response.status_code == HTTP_200_OK

    response_json = response.json()
    for sensor_target_kwargs in response_json:
        assert SensorTargetFactory.build(**sensor_target_kwargs) in sensor_targets
