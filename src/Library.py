import requests

class Library:
    def __init__(self):
        self._base_url = "http://localhost:5000"
        self.reset_application()

    def reset_application(self):
        requests.post(f"{self._base_url}/tests/reset")


    def add_book(self, title, author, isbn, year, publisher):
        data = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "year": year,
            "publisher": publisher,
        }

        requests.post(f"{self._base_url}/add_new", data=data)