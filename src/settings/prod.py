import os
from settings.base import *


ALLOWED_HOSTS = [
    "load_balancer",
    "localhost",
    "192.168.68.129",
    "192.168.68.117",
    "home-server",
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
