from app import app
from flask import render_template, redirect, request, make_response, flash
from entries import add_book
@app.route("/")
def index():
    return render_template("index.html")

        


@app.route("/add_new", methods=["GET", "POST"])
def add_new():
    if request.method == "GET":
        return render_template("add_new.html")
    else:
        #riku/ville?
        #type_ = 
        title = request.form["title"]
        author_list = request.form["author"]
        isbn = request.form["isbn"]
        year = request.form["year"]
        publisher = request.form["publisher"]
        keywords_list = request.form["keywords"]

        # tietokantaoperaatiot?
        add_book(author_list, title,publisher,year,isbn)
        #flash("Lisäys onnistui! tms")
        return redirect("/")







