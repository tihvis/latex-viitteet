from app import app
from flask import flash, render_template, redirect, request, make_response
from entries import add_book, get_all_citations
import re

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
        #keywords_list = request.form["keywords"]
        if not (1 <= len(title) <= 80):
            return render_template("error.html", error="Kirjan otsikon tulee olla 1-80 merkkiä pitkä.")
        if not (5 <= len(isbn) <= 17) or not re.match("^[0-9-]+$", isbn):
            return render_template("error.html", error="ISBN-koodin tulee olla 5-17 merkkiä pitkä, ja koostua vain numeroista ja viivoista.")
        if year == "" or not (1 <= int(year) <= 2025) or not year.isdigit():
            return render_template("error.html", error="Vuosiluku ei kelpaa.")
        if not (2 <= len(publisher) <= 40):
            return render_template("error.html", error="Kustantajan nimen tulee olla 2-40 merkkiä pitkä.")
        if len(author_list) == 0:
            return render_template("error.html", error="Viitteeseen tulee lisätä vähintään yksi kirjailija.")
        for author in author_list:
            names = author.split()
            if len(names) < 2:
                return render_template("error.html", error="Jokaisen kirjailijan nimessä tulee olla vähintään kaksi nimeä.")
        add_book(title, author_list, isbn, year, publisher)
        flash("Lisäys onnistui!")
        return redirect("/")      
        
    
        #Tähän vielä joku tarkistus onko kyseistä kirjaa jo olemassa tietokannassa.
        #Eli tarkistus onko sama isbn jo lisätty, tai onko sama otsikko+vuosi kombo jo olemassa
        #     return render_template("error.html", error="Kyseinen kirja on jo lisätty tietokantaan, voit hakea lisäämäsi viitteet etusivulta.")


@app.route("/list")
def list():
    citations = get_all_citations()
    return render_template("list.html", citations=citations)
        





