from sqlalchemy.sql import text
from entities.user import User

class UserRepository():
    """Luokka käyttäjien lisäämistä, poistamista ja muokkausta varten tietokannassa"""
    def __init__(self, db) -> None:
        self._db = db

    def get_user_by_id_from_database(self, user_uuid : str):
        sql = text("SELECT uuid, username, password_hash FROM users WHERE uuid=:uuid")
        result = self._db.session.execute(sql, {"uuid" : user_uuid}).fetchall()
        if len(result) < 1:
            return None
        result = result[0]
        return User(result[0], result[1], result[2])

    def get_user_by_username_from_database(self, username: str):
        sql = text("SELECT uuid, username, password_hash FROM users WHERE username=:username")
        result = self._db.session.execute(sql, {"username":username}).fetchall()
        if len(result) < 1:
            return None
        result = result[0]
        return User(result[0], result[1], result[2])

    def create_user_in_database(self, user : User):
        try:
            sql = text("INSERT INTO users (uuid, username, password_hash) VALUES (:uuid, :username, :password_hash)")
            self._db.session.execute(sql, {"uuid": user.get_id(), "username": user.username, "password_hash": user.password_hash})
            self._db.session.commit()
        except:
            return False
        return True

    def delete_user_from_database(self, user : User):
        #sql = text("DELETE FROM users WHERE uuid=:uuid RETURNING *")
        #result = self._db.session.execute(sql, {"uuid" : user.get_id()}).fetchall()[0]
        pass

    def update_user_data(self, user : User):
        pass

    def is_username_taken(self, username : str):
        sql = text("SELECT COUNT(*) FROM users WHERE LOWER(username)=LOWER(:username)")
        result = self._db.session.execute(sql, {"username" : username}).fetchall()[0]
        return result[0] > 0

    def does_user_already_exist(self, user_uuid : str):
        sql = text("SELECT uuid FROM users WHERE uuid=:uuid")
        result = self._db.session.execute(sql, {"uuid" : user_uuid}).fetchall()[0]
        if len(result) < 1:
            return False
        return True
