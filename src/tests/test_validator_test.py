import unittest
#from flaskapp.routes import EntryValidator
from flaskapp.validator import EntryValidator

class TestValidator(unittest.TestCase):
    def test_tavallinen_kirja_validoi(self):
        validator = EntryValidator()
        expected = (True, "")
        output = validator.validate_book(["J. R. R. Tolkien"], "Taru sormusten herrasta", "1954", "Allen & Unwin")
        self.assertEqual(expected, output)
    
    def test_liian_lyhyt_kirjan_nimi(self):
        validator = EntryValidator()
        expected = (False, "Kirjan otsikon tulee olla 1-80 merkkiä pitkä.")
        output = validator.validate_book(["J. R. R. Tolkien"], "", "1954", "Allen & Unwin")
        self.assertEqual(expected, output)

    #def test_huono_isbn(self):
    #    validator = EntryValidator()
    #    expected = (False, "ISBN-koodin tulee olla 5-17 merkkiä pitkä, ja koostua vain numeroista ja viivoista.")
    #    output = validator.validate(["J. R. R. Tolkien"], "Taru sormusten herrasta", "1954", "Allen & Unwin", "fjsdskhfsdkhdlsajdas")
    #    self.assertEqual(expected, output)

    def test_liian_liian_lyhyt_kustantaja(self):
        validator = EntryValidator()
        expected = (False, "Kustantajan nimen tulee olla 2-40 merkkiä pitkä.")
        output = validator.validate_book(["J. R. R. Tolkien"], "Taru sormusten herrasta", "1954", "")
        self.assertEqual(expected, output)

    def test_ei_kirjailijaa(self):
        validator = EntryValidator()
        expected = (False, "Viitteeseen tulee lisätä vähintään yksi kirjailija.")
        output = validator.validate_book([], "Taru sormusten herrasta", "1954", "Allen & Unwin")
        self.assertEqual(expected, output)

    def test_huono_vuosiluku(self):
        validator = EntryValidator()
        expected = (False, "Vuosiluku ei kelpaa.")
        output = validator.validate_book(["Kalle Kalastaja"], "Kallen kalapaikat", -5, "Otava")
        self.assertEqual(expected, output)

    def test_tavallinen_artikkeli_validoi(self):
        validator = EntryValidator()
        author_list, title, journal = ["Antti Ahkera"], "Hometalot", "Kotiliesi"
        year, volume, pages = "2020", "186", "25-30"
        expected = (True, "")
        output = validator.validate_article(author_list, title, journal, year, volume, pages)
        self.assertEqual(expected, output)

    def test_kirjalija_puuttuu(self):
        validator = EntryValidator()
        author_list, title, journal = [], "Hometalot", "Kotiliesi"
        year, volume, pages = "2020", "186", "25-30"
        expected = (False, "Viitteeseen tulee lisätä vähintään yksi kirjailija.")
        output = validator.validate_article(author_list, title, journal, year, volume, pages)
        self.assertEqual(expected, output)

    def test_title_liian_lyhyt(self):
        validator = EntryValidator()
        author_list, title, journal = ["Antti Ahkera"], "", "Kotiliesi"
        year, volume, pages = "2020", "186", "25-30"
        expected = (False, "Artikkelin otsikon tulee olla 1-80 merkkiä pitkä.")
        output = validator.validate_article(author_list, title, journal, year, volume, pages)
        self.assertEqual(expected, output)

    def test_journalissa_vikaa(self):
        validator = EntryValidator()
        author_list, title, journal = ["Antti Ahkera"], "Hometalot", ""
        year, volume, pages = "2020", "186", "25-30"
        expected = (False, "Lehden nimen tulee olla 1-80 merkkiä pitkä.")
        output = validator.validate_article(author_list, title, journal, year, volume, pages)
        self.assertEqual(expected, output)

    def test_viallinen_vuosiluku(self):
        validator = EntryValidator()
        author_list, title, journal = ["Antti Ahkera"], "Hometalot", "Kotiliesi"
        year, volume, pages = "-5", "186", "25-30"
        expected = (False, "Vuosiluku ei kelpaa.")
        output = validator.validate_article(author_list, title, journal, year, volume, pages)
        self.assertEqual(expected, output)

    def test_viallinen_vuosikerta(self):
        validator = EntryValidator()
        author_list, title, journal = ["Antti Ahkera"], "Hometalot", "Kotiliesi"
        year, volume, pages = "2020", "-186", "25-30"
        expected = (False, "Vuosikerta ei kelpaa.")
        output = validator.validate_article(author_list, title, journal, year, volume, pages)
        self.assertEqual(expected, output)

    def test_viallinen_sivunumero(self):
        validator = EntryValidator()
        author_list, title, journal = ["Antti Ahkera"], "Hometalot", "Kotiliesi"
        year, volume, pages = "2020", "186", "25,30"
        expected = (False, "Ilmoita sivunumerot muodossa 38-42.")
        output = validator.validate_article(author_list, title, journal, year, volume, pages)
        self.assertEqual(expected, output)

