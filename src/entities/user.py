class User():
    def __init__(self) -> None:
        self._id = None
        self._username = None
        self._password = None

    def check_password(self, password):
        # Passwords should be store as a hash
        # Check password string compared to hash
        # TODO: Find library for password encryption and login
        # Vanilla flask is also a possibility
        pass


    def set_password(self, password):
        pass
    