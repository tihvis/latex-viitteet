import requests

class Library:
    def __init__(self):
        self._base_url = "http://localhost:5000"
        self.reset_application()

    def reset_application(self):
        requests.post(f"{self._base_url}/tests/reset")


#Tätä alla olevaa ei ole testattu, koska tässä branchissa ei 
#ollut entries.py jostain syystä
    def add_book(authors, title, publisher, year, isbn):
        data = {
            "authors": authors,
            "title": title,
            "publisher": publisher,
            "year": year,
            "isbn": isbn
        }

        requests.post(f"{self._base_url}/add_new", data=data)