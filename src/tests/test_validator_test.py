import unittest
from flaskapp.routes import EntryValidator

class TestValidator(unittest.TestCase):
    def test_tavallinen_kirja_validoi(self):
        validator = EntryValidator()
        expected = (True, "")
        output = validator.validate(["J. R. R. Tolkien"], "Taru sormusten herrasta", "1954", "Allen & Unwin", "0008471290")
        self.assertEqual(expected, output)