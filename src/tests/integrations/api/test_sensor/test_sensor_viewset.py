import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test__sensor_viewset__list_should_return_multiple_sensors(
    auth_api: APIClient,
):
    pass
