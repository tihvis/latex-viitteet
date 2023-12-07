from flask import (
    Response,
    flash,
    render_template,
    redirect,
    request,
)
from flask.views import View
from flask_login import current_user, login_required, login_user, logout_user

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
    decorators = [login_required]

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
        if self._citation_service.add_citation(current_user, request.form):
            flash("Lisäys onnistui!")
            return redirect("/")

        return render_template(
            "error.html",
            error="Kyseinen kirja on jo lisätty tietokantaan, \
                voit hakea lisäämäsi viitteet etusivulta.",
        )


class AddInproceedingsView(View):
    methods = ["GET", "POST"]
    decorators = [login_required]

    def __init__(self, citation_service, entry_validator, template) -> None:
        self._citation_service = citation_service
        self._template = template
        self._validator = entry_validator

    def dispatch_request(self):
        if request.method == "GET":
            return render_template(self._template)
        msg_tuple = self._validator.validate_inproceedings(request.form)
        if not msg_tuple[0]:
            return render_template("error.html", error=msg_tuple[1])
        if self._citation_service.add_citation(current_user, request.form):
            flash("Lisäys onnistui!")
            return redirect("/")

        return render_template(
            "error.html",
            error="Kyseinen konferenssiartikkeli on jo lisätty tietokantaan, \
                voit hakea lisäämäsi viitteet etusivulta.",
        )


class AddArticleView(View):
    methods = ["GET", "POST"]
    decorators = [login_required]

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
        if self._citation_service.add_citation(current_user, request.form):
            flash("Lisäys onnistui!")
            return redirect("/")

        return render_template(
            "error.html",
            error="Kyseinen artikkeli on jo lisätty tietokantaan, \
                voit hakea lisäämäsi viitteet etusivulta.",
        )


class ListView(View):
    decorators = [login_required]

    def __init__(self, citation_service, template):
        self._citation_service = citation_service
        self._template = template

    def dispatch_request(self):
        items = self._citation_service.list_citations(current_user)
        return render_template(self._template, citations=items, amount=len(items))


class ErrorView(View):
    def __init__(self, error_msg, template):
        self._error_msg = error_msg
        self._template = template

    def dispatch_request(self):
        items = self._error_msg
        return render_template(self._template, items=items)


class DownloadView(View):
    decorators = [login_required]

    def __init__(self, citation_service, exporter):
        self._citation_service = citation_service
        self._exporter = exporter

    def dispatch_request(self):
        citations = self._citation_service.list_citations(current_user)
        result = self._exporter.bibobject_list_to_text(citations)
        return Response(
            result,
            mimetype="text/plain",
            headers={"Content-disposition": "attachment; filename=citations.bib"},
        )


class RegisterView(View):
    methods = ["GET", "POST"]

    def __init__(self, user_service, entry_validator, template) -> None:
        self._user_service = user_service
        self._template = template
        self._validator = entry_validator

    def dispatch_request(self):
        if request.method == "GET":
            return render_template(self._template)
        msg_tuple = self._validator.validate_credentials(request.form)
        if not msg_tuple[0]:
            return render_template("error.html", error=msg_tuple[1])

        username = request.form.get("username")
        password = request.form.get("password")
        if self._user_service.create_new_user(username, password):
            flash("Rekisteröityminen onnistui, voit nyt kirjautua sisään!")
            return redirect("/")

        return render_template(
            "error.html",
            error="Käyttäjätunnus on jo olemassa, kokeile rekisteröitymistä toisella käyttäjätunnuksella.",
        )


class LoginView(View):
    methods = ["GET", "POST"]

    def __init__(self, user_service, login_manager, template) -> None:
        self._user_service = user_service
        self._template = template
        self._login_manager = login_manager

    def dispatch_request(self):
        if request.method == "GET":
            return render_template(self._template)
        username = request.form.get("username")
        password = request.form.get("password")
        user = self._user_service.get_user_by_username(username)
        if self._user_service.check_user_credentials(username, password, user):
            login_user(user)
            flash("Sisäänkirjautuminen onnistui!")
            return redirect("/")
        flash("Sisäänkirjautuminen ei onnistunut.")
        return redirect("/")


class LogoutView(View):
    def dispatch_request(self):
        logout_user()
        flash("Uloskirjautuminen onnistui!")
        return redirect("/")
