from flask_login import UserMixin

class User(UserMixin):
    """Käyttäjä luokka, sisältää käyttäjän id, nimen ja salasanan."""
    def __init__(self, id, username, password_hash) -> None:
        self._id = id 
        self._username = username
        self._password_hash = password_hash

    @property
    def username(self):
        return self._username
    
    def get_id(self):
        return self._id

    @property
    def password_hash(self):
        return self._password_hash
    
    def set_password_hash(self, password_hash):
        self._password_hash = password_hash
