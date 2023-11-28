from os import getenv
from routes import IndexView, AddBookView, AddArticleView, ListView, EntryValidator
from entries import Database
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#from sqlalchemy.sql import text

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://"

app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")


db = SQLAlchemy(app)
db_relay = Database(db)

app.add_url_rule(
    "/",
    view_func=IndexView.as_view("index", "index.html"),
)

app.add_url_rule(
    "/add_new_book",
    view_func=AddBookView.as_view("add_new_book", db_relay, EntryValidator(), "add_new_book.html"),
)

app.add_url_rule(
    "/add_new_article",
    view_func=AddArticleView.as_view("add_new_article", db_relay, EntryValidator(),
         "add_new_article.html"),
)

app.add_url_rule(
    "/list",
    view_func=ListView.as_view("list", db_relay, "list.html"),
)
