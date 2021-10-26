from django.urls.base import reverse
import pytest

from django.contrib.auth import get_user_model


@pytest.fixture()
def api_key(client):
    test_user = "user"
    test_password = "test1234!!!"

    register_response = client.post(
        reverse("rest_register"),
        {
            "username": test_user,
            "email": "test@test.com",
            "password1": test_password,
            "password2": test_password,
        },
    )
    assert register_response.status_code == 201

    login_response = client.post(
        reverse("rest_login"),
        {
            "username": test_user,
            "password": test_password,
        },
    )

    assert login_response.status_code == 200
    yield login_response.json()["key"]

    get_user_model().objects.all().delete()
