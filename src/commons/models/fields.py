from django.db.models import fields

from commons.helpers.cryptography_helper import CryptographyHelper


class EncryptedFieldMixin:
    def __init__(self, *args, **kwargs):
        self._cryptography_helper = CryptographyHelper(filename=kwargs.pop('key_name'))
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        """
        Decrypting value from Database
        """
        value = self._cryptography_helper.decrypt(value)
        return super().get_prep_value(value)

    def get_db_prep_save(self, value, connection):
        """
        Encrypting value just before entering the database
        """
        value = self._cryptography_helper.encrypt(data=value)
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
