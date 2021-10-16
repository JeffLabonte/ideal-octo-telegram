import pytest

from django.db.contrib import User
from pytest_drf import ViewSetTest
from pytest_drf.authentication import AsUser
from pytest_lambda import lambda_fixture

user = lambda_fixture(
    lambda: User.objects.create(
        username="user",
        first_name="John",
        last_name="Doe",
        email="test@test.com",
    )
)


@pytest.mark.django_db
class TestGatewayViewSet(
    ViewSetTest,
    AsUser("user"),
):
    pass
