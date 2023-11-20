from flask import Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import routes

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://"
#app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
#app.secret_key = getenv("SECRET_KEY")
db = SQLAlchemy(app)

@app.route("/")
def index():
    return "Heipparallaa!"


