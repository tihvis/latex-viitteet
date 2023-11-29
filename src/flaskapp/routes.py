import re
from flask import flash, render_template, redirect, request, make_response
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

    def __init__(self, citation_service, entry_validator, template) -> None:
        self._template = template
        self._validator = entry_validator
        self._citation_service = citation_service

    def dispatch_request(self):
        if request.method == "GET":
            return render_template(self._template)
        # riku/ville? olisi näppärää, jos tämä tulisi sisäänkirjautumistietoilla?
        msg_tuple = self._validator.validate_book(request.form)
        if not msg_tuple[0]:
            return render_template("error.html", error=msg_tuple[1])
        if self._citation_service.add_citation(request.form):
            flash("Lisäys onnistui!")
            return redirect("/")

        return render_template(
            "error.html",
            error="Kyseinen kirja on jo lisätty tietokantaan, voit hakea lisäämäsi viitteet etusivulta.",
        )


class AddArticleView(View):
    methods = ["GET", "POST"]

    def __init__(self, citation_service, entry_validator, template) -> None:
        self._citation_service = citation_service
        self._template = template
        self._validator = entry_validator

    def dispatch_request(self):
        if request.method == "GET":
            return render_template(self._template)
        msg_tuple = self._validator.validate_article(request.form)
        if not msg_tuple[0]:
            return render_template("error.html", error=msg_tuple[1])
        if self._citation_service.add_citation(request.form):
            flash("Lisäys onnistui!")
            return redirect("/")

        return render_template(
            "error.html",
            error="Kyseinen artikkeli on jo lisätty tietokantaan, voit hakea lisäämäsi viitteet etusivulta.",
        )


class ListView(View):
    def __init__(self, citation_service, template):
        self._citation_service = citation_service
        self._template = template

    def dispatch_request(self):
        items = self._citation_service.list_citations()
        return render_template(self._template, citations=items, amount=len(items))


class ErrorView(View):
    def __init__(self, error_msg, template):
        self._error_msg = error_msg
        self._template = template

    def dispatch_request(self):
        items = self._error_msg
        return render_template(self._template, items=items)


class EntryValidator:
    def __init__(self) -> None:
        pass

    def validate_book(self, data):
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
            return (False, "Vuosikerta ei kelpaa.")
        if not re.match("^[0-9-]+$", pages):
            return (False, "Ilmoita sivunumerot muodossa 38-42.")
        return (True, "")
