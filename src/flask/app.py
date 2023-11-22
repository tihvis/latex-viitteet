from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.sql import text

app = Flask(__name__)
#app.secret_key = "laita tähän oma secret key"
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://"

app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")

db = SQLAlchemy(app)

import routes