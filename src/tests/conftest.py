import pytest

from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


@pytest.fixture()
def auth_client():
    # TODO Fix login with https://www.django-rest-framework.org/api-guide/testing/
    test_user = "user"
    test_password = "test1234!!!"
    user = get_user_model().objects.create(
        username=test_user,
        password=test_password,
    )
    client = APIClient()
    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    yield client

    get_user_model().objects.all().delete()
