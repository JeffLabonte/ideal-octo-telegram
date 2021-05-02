from cryptography.fernet import Fernet
from django.db.models import fields

from src.settings import settings


class EncryptedFieldMixin:
    def __init__(self, *args, **kwargs):
        self._fernet = Fernet(key=settings.SECRET_KEY)
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        """
        Decrypting value from Database
        """
        value = self._fernet.decrypt(value)
        return super().get_prep_value(value)

    def get_db_prep_save(self, value, connection):
        """
        Encrypting value just before entering the database
        """
        value = self._fernet.encrypt(data=value.encode("utf-8"))
        return super().get_db_prep_save(value, connection)


class EncryptedCharField(
    EncryptedFieldMixin,
    fields.CharField
):
    pass

class EncryptedTextField(
    EncryptedFieldMixin,
    fields.TextField,
):
    pass
