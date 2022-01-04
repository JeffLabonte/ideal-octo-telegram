import json
from django.urls.base import reverse
import pytest
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.test import APIClient
from tests.factories.sensor_factory import SensorFactory

from tests.factories.sensor_report_factory import SensorReportFactory
from tests.factories.sensor_target_factory import SensorTargetFactory


def setup():
    return SensorReportFactory.create_batch(size=3)


@pytest.mark.django_db
def test__sensor_report_viewset__list_sensor_report(
    auth_client: APIClient,
):
    sensor_targets = setup()
    url = reverse("report-list")

    response = auth_client.get(
        path=url,
    )

    assert response.status_code == HTTP_200_OK

    response_json = response.json()
    for sensor_target_kwargs in response_json:
        assert SensorReportFactory.build(**sensor_target_kwargs) in sensor_targets


@pytest.mark.django_db
def test__sensor_report_viewset__create_sensor_report(
    auth_client: APIClient,
):
    sensor = SensorFactory.create()
    target = SensorTargetFactory.create()

    sensor.gateway.save()
    sensor.save()
    target.save()

    target_payload = {
        "value_type": "int",
        "value": "200",
        "sensor": sensor.pk,
        "target": target.pk,
    }

    url = reverse("report-list")
    response = auth_client.post(
        path=url,
        data=json.dumps(target_payload),
        content_type="application/json",
    )

    print(response.data)
    assert response.status_code == HTTP_201_CREATED

    response_json = response.json()

    assert response_json["value_type"] == "int"
    assert response_json["value"] == "200"
    assert response_json.get("id") is None
    assert response_json.get("target") is None
    assert response_json.get("sensor") is None
