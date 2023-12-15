"""Moduli, joka validoi lomakkeesta saadut syötteet"""
import re


class EntryValidator:
    """Luokka, joka validoi lomakkeesta saadut syötteet"""

    def __init__(self) -> None:
        pass


    def validate_length(self, str, min, max, name):
        if not min <= len(str) <= max:
            raise Exception(f"{name} on oltava {min}-{max} merkkiä pitkä.")


    def validate_year(self, year):
        if year == "" or not (1 <= int(year) <= 2025) or not year.isdigit():
            raise Exception("Vuosiluku ei kelpaa.")


    def validate_author_list(self, author_list):
        if len(author_list) == 0:
            raise Exception("Viitteeseen tulee lisätä vähintään yksi kirjailija.")


    def validate_book(self, data):
        """Metodi, joka validoi kirjaviitteen syötteet"""
        title = data["title"]
        year = data["year"]
        publisher = data["publisher"]
        author_list = data["author"]

        try:
            self.validate_length(title, 1, 80, "Kirjan otsikon")
            self.validate_length(publisher, 2, 40, "Kustantajan nimen")
            self.validate_year(year)
            self.validate_author_list(author_list)
        except Exception as e:
            return (False, str(e))

        return (True, "")

    def validate_article(self, data):
        """Metodi, joka validoi artikkeliviitteen syötteet"""
        author_list = data["author"]
        title = data["title"]
        journal = data["journal"]
        year = data["year"]
        volume = data["volume"]
        pages = data["pages"]

        try:
            self.validate_length(title, 1, 80, "Artikkelin otsikon")
            self.validate_length(journal, 1, 80, "Lehden nimen")
            self.validate_year(year)
            self.validate_author_list(author_list)
        except Exception as e:
            return (False, str(e))

        if volume == "" or not volume.isdigit():
            return (False, "Lehden numero ei kelpaa.")
        if not re.match("^[0-9-]+$", pages):
            return (False, "Ilmoita sivunumerot muodossa 38-42 tai 42.")
        return (True, "")

    def validate_inproceedings(self, data):
        """Metodi, joka validoi konferenssiartikkeliviitteen syötteet"""
        title = data["title"]
        year = data["year"]
        booktitle = data["booktitle"]
        author_list = data["author"]

        try:
            self.validate_length(title, 1, 80, "Artikkelin otsikon")
            self.validate_length(booktitle, 2, 40, "Julkaisun nimen")
            self.validate_year(year)
            self.validate_author_list(author_list)
        except Exception as e:
            return (False, str(e))

        return (True, "")

    def validate_credentials(self, data):
        """Metodi, joka validoi käyttäjätunnuksen ja salasanan"""
        username = data["username"]
        password = data["password"]

        try:
            self.validate_length(username, 6, 30, "Käyttäjätunnuksen")
            self.validate_length(password, 8, 30, "Salasanan")
        except Exception as e:
            return (False, str(e))

        if not (
            re.search(r"[a-z]", password)
            and re.search(r"[A-Z]", password)
            and re.search(r"[0-9]", password)
        ):
            return (
                False,
                "Salasanan tulee sisältää vähintään yksi pieni kirjain, yksi iso kirjain sekä yksi numero.",
            )
        return (True, "")
