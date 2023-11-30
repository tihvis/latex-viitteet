'''robot-testeissä tarvittava moduli'''
import requests

class Library:
    '''luokka, joka antaa robot-testeissä tarvittavat asetukset'''
    def __init__(self):
        self._base_url = "http://localhost:5000"
        self.reset_application()

    def reset_application(self):
        requests.post(f"{self._base_url}/tests/reset", timeout=5)


    def add_book(self, title, author, isbn, year, publisher):
        data = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "year": year,
            "publisher": publisher,
        }

        requests.post(f"{self._base_url}/add_new", data=data, timeout=5)
