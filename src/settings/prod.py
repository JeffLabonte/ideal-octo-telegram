import os
from settings.base import *


CURRENT_HOST_NAME = os.environ.get("CURRENT_HOST_NAME", "")

ALLOWED_HOSTS = [
    "load_balancer",
    "localhost",
    "192.168.68.129",
    "192.168.68.117",
    "home-server",
    CURRENT_HOST_NAME,
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ["DATABASE_NAME"],
        "USER": os.environ["DATABASE_USER"],
        "PASSWORD": os.environ["DATABASE_PASSWORD"],
        "HOST": os.environ["DATABASE_HOST"],
        "PORT": "",
    }
}
