'''robot-testeissä tarvittava moduli'''
import os

from sqlalchemy import create_engine, text

class Library:
    '''luokka, joka antaa robot-testeissä tarvittavat asetukset'''
    def __init__(self):
        self._base_url = "http://localhost:5000"
        self.reset_application()

    def reset_application(self):
        pass