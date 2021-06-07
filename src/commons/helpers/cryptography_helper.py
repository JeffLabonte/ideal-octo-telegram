import os

from cryptography.fernet import Fernet

from settings.settings import BASE_DIR


class CryptographyHelper:
    FOLDER_PATH = os.path.join(BASE_DIR, "keys")

    def __init__(self, filename: str):
        self._file_path = os.path.join(self.FOLDER_PATH, filename)
        self._key = self._get_key()
        self._fernet = Fernet(self._key)

    def _get_key(self) -> bytes:
        self._create_folder()
        if os.path.exists(self._file_path):
            with open(self._file_path, mode="rb+") as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(self._file_path, mode="wb+") as f:
                f.write(key)
            return key

    def _create_folder(self):
        if not os.path.exists(self.FOLDER_PATH):
            os.mkdir(self.FOLDER_PATH)

    def encrypt(self, value: str):
        return self._fernet.encrypt(data=value.encode("UTF-8"))

    def decrypt(self, value: str):
        return self._fernet.decrypt(value)
