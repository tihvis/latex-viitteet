'''robot-testeissä tarvittava moduli'''
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import requests
import os

from sqlalchemy import create_engine, text

class Library:
    '''luokka, joka antaa robot-testeissä tarvittavat asetukset'''
    def __init__(self):
        self._base_url = "http://localhost:5000"
        self.reset_application()

    def reset_application(self):
        engine = create_engine("postgresql:///test")
        with engine.begin() as cur:
            cur.execute(text("TRUNCATE citations"))
            cur.commit()
