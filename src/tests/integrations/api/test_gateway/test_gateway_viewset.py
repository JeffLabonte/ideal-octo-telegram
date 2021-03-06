import json

import pytest
from django.urls.base import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.test import APIClient

from gateway.models import Gateway
from sensor.models import Sensor
from tests.factories.gateway_factory import GatewayFactory
from tests.factories.sensor_factory import SensorFactory


def setup():
    gateways = GatewayFactory.create_batch(size=2)
    sensors = [
        SensorFactory.create(
            gateway=gateways[0],
        ),
        SensorFactory.create(
            gateway=gateways[0],
        ),
        SensorFactory.create(
            gateway=gateways[1],
        ),
        SensorFactory.create(
            gateway=gateways[1],
        ),
    ]

    yield gateways, sensors


@pytest.mark.django_db
def test__gateway_viewset__list_gateway(
    auth_client,
):
    gateways, sensors = tuple(setup())[0]

    url = reverse("gateway-list")
    response = auth_client.get(
        path=url,
    )

    assert response.status_code == HTTP_200_OK

    for gateway_response in response.json():
        sensor = Sensor(**gateway_response.pop("sensors", []))
        gateway = Gateway(**gateway_response)

        assert gateway in gateways
        assert sensor in sensors


@pytest.mark.django_db
def test__gateway_viewset__create_gateway(
    auth_client: APIClient,
):
    gateway_payload = {
        "name": "Gateway RPI 1",
        "mac_address": "aa:bb:cc:dd:ee:ff",
        "sensors": [
            {
                "name": "Ambiant Temperature",
                "type": "temperature",
            },
            {
                "name": "Ambiant Relative Humidity",
                "type": "humidity",
            },
        ],
    }

    url = reverse("gateway-list")
    response = auth_client.post(
        path=url,
        data=json.dumps(gateway_payload),
        content_type="application/json",
    )

    assert response.status_code == HTTP_201_CREATED

    response_json = response.json()

    assert response_json["name"] == gateway_payload["name"]
    assert response_json["mac_address"] == gateway_payload["mac_address"]
    assert len(response_json["gateway_sensors"]) == len(gateway_payload["sensors"])
