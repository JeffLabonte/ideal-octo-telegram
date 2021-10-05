import pytest
from django.contrib.auth.models import User
from pytest_drf import Returns201, ViewSetTest
from pytest_drf.authentication import AsUser
from pytest_drf.util.urls import url_for
from pytest_drf.views import UsesListEndpoint, UsesPostMethod
from pytest_lambda import lambda_fixture
from pytest_lambda.fixtures import static_fixture


user = lambda_fixture(
    lambda: User.objects.create(
        username="user",
        first_name="John",
        last_name="Doe",
        email="example@test.com",
    )
)


@pytest.mark.django_db
class TestDeviceViewSet(
    ViewSetTest,
    AsUser("user"),
):
    list_url = lambda_fixture(
        lambda: url_for("devices-list"),
    )

    detail_url = lambda_fixture(
        lambda device: url_for(
            "devices-detail",
            device.pk,
        )
    )

    @pytest.mark.django_db
    class TestCreate(
        UsesPostMethod,
        UsesListEndpoint,
        Returns201,
    ):
        data = static_fixture(
            {
                "device_name": "rpi_downstairs",
            }
        )
