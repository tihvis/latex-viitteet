import unittest
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
        expected = (False, "Kirjan otsikon on oltava 1-80 merkkiä pitkä.")
        book = {"author":"J. R. R. Tolkien", "title":"", "year": "1954", "publisher": "Allen & Unwin"}
        output = validator.validate_book(book)
        self.assertEqual(expected, output)

    def test_liian_liian_lyhyt_kustantaja(self):
        validator = EntryValidator()
        expected = (False, "Kustantajan nimen on oltava 2-40 merkkiä pitkä.")
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
        expected = (False, "Artikkelin otsikon on oltava 1-80 merkkiä pitkä.")
        article = {"author":"Antti Ahkera", "title":"", "journal":"Kotiliesi", "year":"2020", "volume":"186", "pages":"25-30"}
        output = validator.validate_article(article)
        self.assertEqual(expected, output)

    def test_journalissa_vikaa(self):
        validator = EntryValidator()
        expected = (False, "Lehden nimen on oltava 1-80 merkkiä pitkä.")
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

    def test_tavallinen_konf(self):
        validator = EntryValidator()
        expected = (True, "")
        inproceedings = {"author":"Vihavainen, Arto\r\nPaksula, Matti", "title":"Extreme Apprenticeship Method in Teaching Programming for Beginners.", "year": "2011", "booktitle": "SIGCSE '11"}
        output = validator.validate_inproceedings(inproceedings)
        self.assertEqual(expected, output)

    def test_tavallinen_rekisteroityminen(self):
        validator = EntryValidator()
        expected = (True, "")
        credentials = {"username":"Testikayttaja", "password":"SALAs4n4"}
        output = validator.validate_credentials(credentials)
        self.assertEqual(expected, output)

    def test_liian_lyhyt_kayttajatunnus(self):
        validator = EntryValidator()
        expected = (False, "Käyttäjätunnuksen on oltava 6-30 merkkiä pitkä.")
        credentials = {"username":"testi", "password":"SALAs4n4"}
        output = validator.validate_credentials(credentials)
        self.assertEqual(expected, output)

    def test_liian_pitka_kayttajatunnus(self):
        validator = EntryValidator()
        expected = (False, "Käyttäjätunnuksen on oltava 6-30 merkkiä pitkä.")
        credentials = {"username":"Testitestitestitestitestitestit", "password":"SALAs4n4"}
        output = validator.validate_credentials(credentials)
        self.assertEqual(expected, output)

    def test_liian_lyhyt_salasana(self):
        validator = EntryValidator()
        expected = (False, "Salasanan on oltava 8-30 merkkiä pitkä.")
        credentials = {"username":"testikayttaja", "password":"S4las"}
        output = validator.validate_credentials(credentials)
        self.assertEqual(expected, output)

    def test_liian_pitka_salasana(self):
        validator = EntryValidator()
        expected = (False, "Salasanan on oltava 8-30 merkkiä pitkä.")
        credentials = {"username":"testikayttaja", "password":"S4lasanaS4lasanaS4lasanaS4lasan"}
        output = validator.validate_credentials(credentials)
        self.assertEqual(expected, output)

    def test_ei_numeroa_salasanassa(self):
        validator = EntryValidator()
        expected = (False, "Salasanan tulee sisältää vähintään yksi pieni kirjain, yksi iso kirjain sekä yksi numero.")
        credentials = {"username":"testikayttaja", "password":"Salasana"}
        output = validator.validate_credentials(credentials)
        self.assertEqual(expected, output)

    def test_ei_isoa_kirjainta_salasanassa(self):
        validator = EntryValidator()
        expected = (False, "Salasanan tulee sisältää vähintään yksi pieni kirjain, yksi iso kirjain sekä yksi numero.")
        credentials = {"username":"testikayttaja", "password":"s4lasana"}
        output = validator.validate_credentials(credentials)
        self.assertEqual(expected, output)

    def test_ei_pienta_kirjainta_salasanassa(self):
        validator = EntryValidator()
        expected = (False, "Salasanan tulee sisältää vähintään yksi pieni kirjain, yksi iso kirjain sekä yksi numero.")
        credentials = {"username":"testikayttaja", "password":"SALASAN4"}
        output = validator.validate_credentials(credentials)

    def test_viallinen_vuosiluku(self):
        validator = EntryValidator()
        expected = (False, "Vuosiluku ei kelpaa.")
        inproceedings = {"author":"Vihulainen, Arto", "title":"Teaching Programming for Beginners.", "year": "-2011", "booktitle": "SIGCSE '11"}
        output = validator.validate_inproceedings(inproceedings)
        self.assertEqual(expected, output)

    def test_kirjoittajan_nimi_puuttuu(self):
        validator = EntryValidator()
        expected = (False, "Viitteeseen tulee lisätä vähintään yksi kirjailija.")
        inproceedings = {"author":"", "title":"Teaching Programming for Beginners.", "year": "2011", "booktitle": "SIGCSE '11"}
        output = validator.validate_inproceedings(inproceedings)
        self.assertEqual(expected, output)

    def test_artikkelin_nimi_puuttuu(self):
        validator = EntryValidator()
        expected = (False, "Artikkelin otsikon on oltava 1-80 merkkiä pitkä.")
        inproceedings = {"author":"Vihulainen, Arto", "title":"", "year": "2011", "booktitle": "SIGCSE '11"}
        output = validator.validate_inproceedings(inproceedings)
        self.assertEqual(expected, output)

    def test_julkaisun_nimi_puuttuu(self):
        validator = EntryValidator()
        expected = (False, "Julkaisun nimen on oltava 2-40 merkkiä pitkä.")
        inproceedings = {"author":"Vihulainen, Arto", "title":"Teaching Programming for Beginners.", "year": "2011", "booktitle": ""}
        output = validator.validate_inproceedings(inproceedings)
        self.assertEqual(expected, output)
