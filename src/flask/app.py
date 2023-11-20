from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://"
db = SQLAlchemy(app)

@app.route("/")
def index():
    return "Heipparallaa!"

