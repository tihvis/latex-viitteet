from app import app
from flask import flash, render_template, redirect, request, make_response
from entries import add_book, get_all_citations

@app.route("/")
def index():
    return render_template("index.html")

        


@app.route("/add_new_book", methods=["GET", "POST"])
def add_new_book():
    if request.method == "GET":
        return render_template("add_new_book.html")
    else:
        #riku/ville? olisi näppärää, jos tämä tulisi sisäänkirjautumistietoilla?
        type_ = "book"
        title = request.form["title"]
        author_list = request.form["author"]
        isbn = request.form["isbn"]
        year = request.form["year"]
        publisher = request.form["publisher"]
        keywords_list = request.form["keywords"]
        if len(title) < 5:
            flash("Kirjan nimi on liian lyhyt")
            return render_template("/add_new_book.html")
        if len(title) > 50:
            flash("Kirjan nimi on liian pitkä")
            return render_template("/add_new_book.html")
        # tietokantaoperaatiot?
        if not add_book(author_list, title,publisher,year,isbn):
            flash("Lisäys epäonnistui!")
            return render_template("add_new_book.html")
        else:
            flash("Lisäys onnistui!")
            return redirect("/")


@app.route("/list")
def list():
    citations = get_all_citations()
    return render_template("list.html", citations=citations)
        





