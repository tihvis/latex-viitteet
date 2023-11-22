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
            return render_template("/add_new_book")
        if len(title) > 40:
            flash("Kirjan nimi on liian pitkä")
            return render_template("/add_new_book")
        if len(isbn) < 5:
            flash("ISBN-numero on liian lyhyt")
            return render_template("/add_new_book")
        if len(isbn) > 17:
            flash("ISBN-numero on liian pitkä")
            return render_template("/add_new_book")
        if year < 0:
            flash("Vuosiluku ei kelpaa")
            return render_template("/add_new_book")
        if len(publisher) < 5:
            flash("Kustantajan nimi on liian lyhyt")
            return render_template("/add_new_book")
        if len(publisher) > 40:
            flash("Kustantajan nimi on liian pitkä")
            return render_template("/add_new_book")
        #for author in author_list: #tää tuntuu toimivan silloinkin kun ei pitäisi o_O
            #name = author.split(" ")
            #if len(name) == 1:
                #flash("Kirjailijan sukunimi puuttuu")
                #return redirect("/add_new_book")
        
        
        

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
        





