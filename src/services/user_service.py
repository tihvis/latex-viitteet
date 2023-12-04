from entities.user import User
from services.user_crypto_service import UserCryptoService
from repositories.user_repository import UserRepository

class UserService():
    """Luokka käyttäjien lisäämistä, poistamista ja muokkausta varten"""
    def __init__(self, user_repository : UserRepository, crypto_service : UserCryptoService) -> None:
        self._user_repository = user_repository
        self._crypto_service = crypto_service

    def create_new_user(self, username : str, password : str):
        if self._user_repository.is_username_taken(username):
            return
        new_user = User(username, self._crypto_service.get_hash_from_password(password))
        self._user_repository.create_user_in_database(new_user)

    def delete_user(self, user : User):
        self._user_repository.delete_user_from_database(user)

    def get_user_by_id(self, id):
        return self._user_repository.get_user_by_id_from_database()

    def set_user_password(self, user : User, password : str):
        pass