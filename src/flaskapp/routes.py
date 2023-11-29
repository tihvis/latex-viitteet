import re
from flask import flash, render_template, redirect, request, make_response
from flask.views import View

# from validator import EntryValidator

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
