import requests

class Library:
    def __init__(self):
        self._base_url = "http://localhost:5001"
        self.reset_application()
    #tää metodi on pielessä, koska en ymmärrä mitä sen
    #ois tarkoitus tehdä
    def reset_application(self):
        requests.post(f"{self._base_url}/tests/reset")