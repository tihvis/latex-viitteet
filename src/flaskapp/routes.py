from flask import flash, render_template, redirect, request, make_response
import re
from flask.views import View

#
# https://flask.palletsprojects.com/en/2.3.x/views/
#

class IndexView(View):
    def __init__(self, template) -> None:
        self._template = template

    def dispatch_request(self):
        return render_template(self._template)

class AddBookView(View):
    methods = ["GET", "POST"]
    def __init__(self, database_relay, entry_validator, template) -> None:
        self._database_relay = database_relay
        self._template = template
        self._validator = entry_validator

    def dispatch_request(self):
        if request.method == "GET":
            return render_template(self._template)
        else:
            #riku/ville? olisi näppärää, jos tämä tulisi sisäänkirjautumistietoilla?
            type = "book"
            title = str(request.form["title"])
            author_list = str(request.form["author"])
            isbn = str(request.form["isbn"])
            year = str(request.form["year"])
            publisher = str(request.form["publisher"])
            #keywords_list = request.form["keywords"]
            msg_tuple = self._validator.validate(author_list, title, year, publisher, isbn)
            if msg_tuple[0] == False:
                return render_template("error.html", error=msg_tuple[1])
            self._database_relay.add_book(author_list, title, isbn, year, publisher)
            flash("Lisäys onnistui!")
            return redirect("/")      
            #Tähän vielä joku tarkistus onko kyseistä kirjaa jo olemassa tietokannassa.
            #Eli tarkistus onko sama isbn jo lisätty, tai onko sama otsikko+vuosi kombo jo olemassa
            #     return render_template("error.html", error="Kyseinen kirja on jo lisätty tietokantaan, voit hakea lisäämäsi viitteet etusivulta.")

class ListView(View):
    def __init__(self, db, template):
        self._db = db
        self._template = template

    def dispatch_request(self):
        items = self._db.get_all_citations()
        return render_template(self._template, citations=items, amount=len(items))

class ErrorView(View):
    def __init__(self, error_msg, template):
        self._error_msg = error_msg
        self._template = template

    def dispatch_request(self):
        items = self._error_msg
        return render_template(self._template, items=items)

class EntryValidator():
    def __init__(self) -> None:
        pass

    def validate(self, author_list, title, year, publisher, isbn):
        if not (1 <= len(title) <= 80):
            return (False, "Kirjan otsikon tulee olla 1-80 merkkiä pitkä.")
        if not (5 <= len(isbn) <= 17) or not re.match("^[0-9-]+$", isbn):
            return (False, "ISBN-koodin tulee olla 5-17 merkkiä pitkä, ja koostua vain numeroista ja viivoista.")
        if year == "" or not (1 <= int(year) <= 2025) or not year.isdigit():
            return (False, "Vuosiluku ei kelpaa.")
        if not (2 <= len(publisher) <= 40):
            return (False, "Kustantajan nimen tulee olla 2-40 merkkiä pitkä.")
        if len(author_list) == 0:
            return (False, "Viitteeseen tulee lisätä vähintään yksi kirjailija.")
        return (True, "")
        # Väliaikaisesti poistettu
        #for author in author_list:
        #    names = author.split()
            #if len(names) < 2:
            #    return render_template("error.html", error="Jokaisen kirjailijan nimessä tulee olla vähintään kaksi nimeä.")

