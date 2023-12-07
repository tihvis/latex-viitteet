import uuid
import bcrypt

class UserCryptoService():
    """Salasanojen enkryptoinnista vastaava luokka"""
    def __init__(self) -> None:
        self._default_encoder = "utf-8"

    def check_password(self, password : str, hash : str):
        return bcrypt.checkpw(password.encode(self._default_encoder),
            hash.encode(self._default_encoder))

    def create_hash_from_password(self, password : str):
        return str(bcrypt.hashpw(password.encode(self._default_encoder),
            bcrypt.gensalt()).decode(self._default_encoder))

    def create_user_uuid(self):
        return str(uuid.uuid4())
