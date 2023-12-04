from entities.user import User

class UserRepository():
    """Luokka käyttäjien lisäämistä, poistamista ja muokkausta varten tietokannassa"""
    def __init__(self, db) -> None:
        self._db = db

    def get_user_by_id_from_database(self, id):
        pass

    def create_user_in_database(self, user : User):
        pass

    def delete_user_from_database(self, user : User):
        pass

    def is_username_taken(self, username):
        pass