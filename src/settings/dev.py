from settings.base import *


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "ideal-octo-telegram",
        "USER": "dev_user",
        "PASSWORD": "dev_user",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
