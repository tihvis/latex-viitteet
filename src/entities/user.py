class User():
    """Käyttäjä luokka, sisältää käyttäjän id, nimen ja salasanan"""
    def __init__(self, username, password_hash) -> None:
        self._id = None
        self._username = username
        self._password_hash = password_hash

    @property
    def username(self):
        return self._username
    
    @property
    def id(self):
        return self._id

    def check_password(self, password):
        pass
    