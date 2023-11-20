from app import app
from flask import render_template, redirect, request, make_response, flash

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method =="GET":
        return render_template("add_book.html")
    #if request.method == "POST":

