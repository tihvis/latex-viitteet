import unittest
from services.user_service import UserService
from entities.user import User

class MockUserRepository():
    def __init__(self) -> None:
        self.users : dict = {
            "removalname" : User("1aca1cb2-509b-4322-a9b4-42343909dbaf", "removalname", "$2b$12$7qX1hyoNtYwp.Z1fbBdSj.MurAj9pdYB8o7O2iEL.4ykFotByeB7e"),
            "testname" : User("1aca1cb2-509b-4322-a9b4-42343909dbaf", "testname", "$2b$12$7qX1hyoNtYwp.Z1fbBdSj.MurAj9pdYB8o7O2iEL.4ykFotByeB7e"),
            "takenname" : User("1aca1cb2-509b-4322-a9b4-42343909dbaf", "takenname", "$2b$12$7qX1hyoNtYwp.Z1fbBdSj.MurAj9pdYB8o7O2iEL.4ykFotByeB7e")
        }

    def get_user_by_id_from_database(self, user_uuid : str):
        pass

    def get_user_by_username_from_database(self, username: str):
        return self.users[username]

    def create_user_in_database(self, user : User):
        return True

    def does_user_already_exist(self, user_uuid : str):
        pass

    def delete_user_from_database(self, user : User):
        self.users.pop(user.username)

    def is_username_taken(self, username : str):
        if username == "takenusername":
            return True
        return False

class MockCryptoService():
    def __init__(self) -> None:
        pass

    def check_password(self, password : str, hash : str):
        pass
    
    def create_hash_from_password(self, password : str):
        return "$2b$12$VS07ZDXOwgnAv8sWELkw9eV.J0DYUm32LlnNe4Ra23k4XmDdwzyN2"
    
    def create_user_uuid(self):
        return "1aca1cb2-509b-4322-a9b4-42343909dbaf"

class TestUserService(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def test_create_new_user(self):
        us = UserService(MockUserRepository(), MockCryptoService())
        result = us.create_new_user("testname", "Password123")
        expected = True
        self.assertEqual(expected, result)

    def test_create_new_user_taken_username(self):
        us = UserService(MockUserRepository(), MockCryptoService())
        result = us.create_new_user("takenusername", "Password123")
        expected = False
        self.assertEqual(expected, result)
    
    def test_delete_user_existing(self):
        mr = MockUserRepository()
        mcs = MockCryptoService()
        us = UserService(mr, mcs)
        us.delete_user(User("1aca1cb2-509b-4322-a9b4-42343909dbaf", "removalname", "$2b$12$VS07ZDXOwgnAv8sWELkw9eV.J0DYUm32LlnNe4Ra23k4XmDdwzyN2"))
        result = "removalname" in mr.users.keys()
        expected = False
        self.assertEqual(expected, result)
    
    def test_get_user_by_username(self):
        mr = MockUserRepository()
        mcs = MockCryptoService()
        us = UserService(mr, mcs)
        result = us.get_user_by_username("testname")
        expected = User("1aca1cb2-509b-4322-a9b4-42343909dbaf", "testname", "$2b$12$7qX1hyoNtYwp.Z1fbBdSj.MurAj9pdYB8o7O2iEL.4ykFotByeB7e")
        self.assertAlmostEqual(expected, result)
