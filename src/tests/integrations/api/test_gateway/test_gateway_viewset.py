import pytest
from django.urls.base import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.test import APIClient

from gateway.models import Gateway
from sensor.models import Sensor


def setup():
    gateways = [
        Gateway.objects.create(
            name="Gateway Test 1",
            mac_address="aa:bb:cc:dd:ee:ff",
        ),
        Gateway.objects.create(
            name="Gateway Test 2",
            mac_address="aa:bb:cc:dd:dd:ff",
        ),
    ]
    sensors = [
        Sensor.objects.create(
            type="temperature",
            gateway=gateways[0],
        ),
        Sensor.objects.create(
            type="humdity",
            gateway=gateways[0],
        ),
        Sensor.objects.create(
            type="temperature",
            gateway=gateways[1],
        ),
        Sensor.objects.create(
            type="humdity",
            gateway=gateways[1],
        ),
    ]

    yield gateways, sensors

    for gateway in gateways:
        gateway.delete()


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
                "type": "temperature",
            },
        ],
    }

    url = reverse("gateway-list")
    response = auth_client.post(
        path=url,
        data=gateway_payload,
    )

    assert response.status_code == HTTP_201_CREATED
