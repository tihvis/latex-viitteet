'''Moduli, joka validoi lomakkeesta saadut syötteet'''
import re

class EntryValidator:
    '''Luokka, joka validoi lomakkeesta saadut syötteet'''
    def __init__(self) -> None:
        pass

    def validate_book(self, data):
        '''Metodi, joka validoi kirjaviitteen syötteet'''
        title = data["title"]
        year = data["year"]
        publisher = data["publisher"]
        author_list = data["author"]

        if not 1 <= len(title) <= 80:
            return (False, "Kirjan otsikon tulee olla 1-80 merkkiä pitkä.")
        # if not (5 <= len(isbn) <= 17) or not re.match("^[0-9-]+$", isbn):
        #    return (False,
        #    "ISBN-koodin tulee olla 5-17 merkkiä pitkä, ja koostua vain numeroista ja viivoista.")
        if year == "" or not (1 <= int(year) <= 2025) or not year.isdigit():
            return (False, "Vuosiluku ei kelpaa.")
        if not 2 <= len(publisher) <= 40:
            return (False, "Kustantajan nimen tulee olla 2-40 merkkiä pitkä.")
        if len(author_list) == 0:
            return (False, "Viitteeseen tulee lisätä vähintään yksi kirjailija.")
        return (True, "")
        # Väliaikaisesti poistettu
        # for author in author_list:
        #    names = author.split()
        # if len(names) < 2:
        #    return render_template("error.html", error="Jokaisen kirjailijan
        #  nimessä tulee olla vähintään kaksi nimeä.")

    def validate_article(self, data):
        '''Metodi, joka validoi artikkeliviitteen syötteet'''
        author_list = data["author"]
        title = data["title"]
        journal = data["journal"]
        year = data["year"]
        volume = data["volume"]
        pages = data["pages"]
        if not 1 <= len(title) <= 80:
            return (False, "Artikkelin otsikon tulee olla 1-80 merkkiä pitkä.")
        if len(author_list) == 0:
            return (False, "Viitteeseen tulee lisätä vähintään yksi kirjailija.")
        if not 1 <= len(journal) <= 80:
            return (False, "Lehden nimen tulee olla 1-80 merkkiä pitkä.")
        if year == "" or not (1 <= int(year) <= 2025) or not year.isdigit():
            return (False, "Vuosiluku ei kelpaa.")
        if volume == "" or not volume.isdigit():
            return (False, "Lehden numero ei kelpaa.")
        if not re.match("^[0-9-]+$", pages):
            return (False, "Ilmoita sivunumerot muodossa 38-42 tai 42.")
        return (True, "")
