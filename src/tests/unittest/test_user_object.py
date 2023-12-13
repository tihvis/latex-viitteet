import unittest
from entities.user import User

class TestUserObject(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.default_uuid = "1aca1cb2-509b-4322-a9b4-42343909dbaf"
        self.default_username = "testname"
        self.default_password_hash = "$2b$12$7qX1hyoNtYwp.Z1fbBdSj.MurAj9pdYB8o7O2iEL.4ykFotByeB7e"
    
    def test_user_object_get_username(self):
        new_user = User("1aca1cb2-509b-4322-a9b4-42343909dbaf", "testname", "$2b$12$7qX1hyoNtYwp.Z1fbBdSj.MurAj9pdYB8o7O2iEL.4ykFotByeB7e")
        self.assertEqual("testname", new_user.username)
    
    def test_user_object_get_id(self):
        new_user = User("1aca1cb2-509b-4322-a9b4-42343909dbaf", "testname", "$2b$12$7qX1hyoNtYwp.Z1fbBdSj.MurAj9pdYB8o7O2iEL.4ykFotByeB7e")
        self.assertEqual("1aca1cb2-509b-4322-a9b4-42343909dbaf", new_user.get_id())
    
    def test_user_object_get_password_hash(self):
        new_user = User("1aca1cb2-509b-4322-a9b4-42343909dbaf", "testname", "$2b$12$7qX1hyoNtYwp.Z1fbBdSj.MurAj9pdYB8o7O2iEL.4ykFotByeB7e")
        self.assertEqual("$2b$12$7qX1hyoNtYwp.Z1fbBdSj.MurAj9pdYB8o7O2iEL.4ykFotByeB7e", new_user.password_hash)
    
    def test_user_object_set_password_hash(self):
        new_user = User("1aca1cb2-509b-4322-a9b4-42343909dbaf", "testname", "$2b$12$7qX1hyoNtYwp.Z1fbBdSj.MurAj9pdYB8o7O2iEL.4ykFotByeB7e")
        new_user.set_password_hash("$2b$12$VS07ZDXOwgnAv8sWELkw9eV.J0DYUm32LlnNe4Ra23k4XmDdwzyN2")
        self.assertEqual("$2b$12$VS07ZDXOwgnAv8sWELkw9eV.J0DYUm32LlnNe4Ra23k4XmDdwzyN2", new_user.password_hash)
        