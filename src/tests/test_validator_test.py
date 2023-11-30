import unittest
#from flaskapp.routes import EntryValidator
from flaskapp.validator import EntryValidator

class TestValidator(unittest.TestCase):
    def test_tavallinen_kirja_validoi(self):
        validator = EntryValidator()
        expected = (True, "")
        book = {"author":"J. R. R. Tolkien", "title":"Taru sormusten herrasta", "year": "1954", "publisher": "Allen & Unwin"}
        output = validator.validate_book(book)
        self.assertEqual(expected, output)
    
    def test_liian_lyhyt_kirjan_nimi(self):
        validator = EntryValidator()
        expected = (False, "Kirjan otsikon tulee olla 1-80 merkkiä pitkä.")
        book = {"author":"J. R. R. Tolkien", "title":"", "year": "1954", "publisher": "Allen & Unwin"}
        output = validator.validate_book(book)
        self.assertEqual(expected, output)

    #def test_huono_isbn(self):
    #    validator = EntryValidator()
    #    expected = (False, "ISBN-koodin tulee olla 5-17 merkkiä pitkä, ja koostua vain numeroista ja viivoista.")
    #    output = validator.validate(["J. R. R. Tolkien"], "Taru sormusten herrasta", "1954", "Allen & Unwin", "fjsdskhfsdkhdlsajdas")
    #    self.assertEqual(expected, output)

    def test_liian_liian_lyhyt_kustantaja(self):
        validator = EntryValidator()
        expected = (False, "Kustantajan nimen tulee olla 2-40 merkkiä pitkä.")
        book = {"author":"J. R. R. Tolkien", "title":"Taru sormusten herrasta", "year": "1954", "publisher": ""}
        output = validator.validate_book(book)
        self.assertEqual(expected, output)

    def test_ei_kirjailijaa(self):
        validator = EntryValidator()
        expected = (False, "Viitteeseen tulee lisätä vähintään yksi kirjailija.")
        book = {"author":"", "title":"Taru sormuste herrasta", "year": "1954", "publisher": "Allen & Unwin"}
        output = validator.validate_book(book)
        self.assertEqual(expected, output)

    def test_huono_vuosiluku(self):
        validator = EntryValidator()
        expected = (False, "Vuosiluku ei kelpaa.")
        book = {"author":"J. R. R. Tolkien", "title":"Taru sormusten herrasta", "year": -5, "publisher": "Allen & Unwin"}
        output = validator.validate_book(book)
        self.assertEqual(expected, output)

    def test_tavallinen_artikkeli_validoi(self):
        validator = EntryValidator()
        expected = (True, "")
        article = {"author":"Antti Ahkera", "title":"Hometalot", "journal":"Kotiliesi", "year":"2020", "volume":"186", "pages":"25-30"}
        output = validator.validate_article(article)
        self.assertEqual(expected, output)

    def test_kirjalija_puuttuu(self):
        validator = EntryValidator()
        expected = (False, "Viitteeseen tulee lisätä vähintään yksi kirjailija.")
        article = {"author":"", "title":"Hometalot", "journal":"Kotiliesi", "year":"2020", "volume":"186", "pages":"25-30"}
        output = validator.validate_article(article)
        self.assertEqual(expected, output)

    def test_title_liian_lyhyt(self):
        validator = EntryValidator()
        expected = (False, "Artikkelin otsikon tulee olla 1-80 merkkiä pitkä.")
        article = {"author":"Antti Ahkera", "title":"", "journal":"Kotiliesi", "year":"2020", "volume":"186", "pages":"25-30"}
        output = validator.validate_article(article)
        self.assertEqual(expected, output)

    def test_journalissa_vikaa(self):
        validator = EntryValidator()
        expected = (False, "Lehden nimen tulee olla 1-80 merkkiä pitkä.")
        article = {"author":"Antti Ahkera", "title":"Hometalot", "journal":"", "year":"2020", "volume":"186", "pages":"25-30"}
        output = validator.validate_article(article)
        self.assertEqual(expected, output)

    def test_viallinen_vuosiluku(self):
        validator = EntryValidator()
        expected = (False, "Vuosiluku ei kelpaa.")
        article = {"author":"Antti Ahkera", "title":"Hometalot", "journal":"Kotiliesi", "year":"-5", "volume":"186", "pages":"25-30"}
        output = validator.validate_article(article)
        self.assertEqual(expected, output)

    def test_viallinen_vuosikerta(self):
        validator = EntryValidator()
        expected = (False, "Lehden numero ei kelpaa.")
        article = {"author":"Antti Ahkera", "title":"Hometalot", "journal":"Kotiliesi", "year":"2020", "volume":"-186", "pages":"25-30"}
        output = validator.validate_article(article)
        self.assertEqual(expected, output)

    def test_viallinen_sivunumero(self):
        validator = EntryValidator()
        expected = (False, "Ilmoita sivunumerot muodossa 38-42 tai 42.")
        article = {"author":"Antti Ahkera", "title":"Hometalot", "journal":"Kotiliesi", "year":"2020", "volume":"186", "pages":"25,30"}
        output = validator.validate_article(article)
        self.assertEqual(expected, output)

