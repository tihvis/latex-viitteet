from flask_login import UserMixin

class User(UserMixin):
    """Käyttäjä luokka, sisältää käyttäjän id, nimen ja salasanan. id on flask_login moduulin luoma, saa kutsumalla User.get_id()"""
    def __init__(self, username, password_hash) -> None:
        self._username = username
        self._password_hash = password_hash

    @property
    def username(self):
        return self._username
