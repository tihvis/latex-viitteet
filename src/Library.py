import requests

class Library:
    def __init__(self):
        self._base_url = "http://localhost:5000"
        self.reset_application()

    def reset_application(self):
        requests.post(f"{self._base_url}/tests/reset")


#Tätä alla olevaa ei ole testattu, koska tässä branchissa ei 
#ollut entries.py jostain syystä
    def add_book(self, title, author, isbn, year, publisher, keywords):
        data = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "year": year,
            "publisher": publisher,
            "keywords": keywords
        }

        requests.post(f"{self._base_url}/add_new", data=data)