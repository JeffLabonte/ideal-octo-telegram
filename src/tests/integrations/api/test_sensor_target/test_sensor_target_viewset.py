import json
from django.urls.base import reverse
import pytest
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
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


@pytest.mark.django_db
def test__sensor_target_viewset__create_sensor_target(
    auth_client: APIClient,
):
    target_payload = {
        "type": "plant",
        "name": "Indica Plant 1",
    }

    url = reverse("target-list")
    response = auth_client.post(
        path=url,
        data=json.dumps(target_payload),
        content_type="application/json",
    )

    assert response.status_code == HTTP_201_CREATED

    response_json = response.json()

    assert response_json["name"] == "Indica Plant 1"
    assert response_json["type"] == "plant"
