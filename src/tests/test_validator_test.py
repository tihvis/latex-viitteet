import unittest
from flaskapp.routes import EntryValidator

class TestValidator(unittest.TestCase):
    def test_tavallinen_kirja_validoi(self):
        validator = EntryValidator()
        expected = (True, "")
        output = validator.validate(["J. R. R. Tolkien"], "Taru sormusten herrasta", "1954", "Allen & Unwin", "0008471290")
        self.assertEqual(expected, output)
    
    def test_liian_lyhyt_kirjan_nimi(self):
        validator = EntryValidator()
        expected = (False, "Kirjan otsikon tulee olla 1-80 merkkiä pitkä.")
        output = validator.validate(["J. R. R. Tolkien"], "", "1954", "Allen & Unwin", "0008471290")
        self.assertEqual(expected, output)

    def test_huono_isbn(self):
        validator = EntryValidator()
        expected = (False, "ISBN-koodin tulee olla 5-17 merkkiä pitkä, ja koostua vain numeroista ja viivoista.")
        output = validator.validate(["J. R. R. Tolkien"], "Taru sormusten herrasta", "1954", "Allen & Unwin", "fjsdskhfsdkhdlsajdas")
        self.assertEqual(expected, output)

    def test_liian_liian_lyhyt_kustantaja(self):
        validator = EntryValidator()
        expected = (False, "Kustantajan nimen tulee olla 2-40 merkkiä pitkä.")
        output = validator.validate(["J. R. R. Tolkien"], "Taru sormusten herrasta", "1954", "", "0008471290")
        self.assertEqual(expected, output)

    def test_ei_kirjailijaa(self):
        validator = EntryValidator()
        expected = (False, "Viitteeseen tulee lisätä vähintään yksi kirjailija.")
        output = validator.validate([], "Taru sormusten herrasta", "1954", "Allen & Unwin", "0008471290")
        self.assertEqual(expected, output)