import requests

class Library:
    def __init__(self):
        self._base_url = "http://lovalhost:5001"
        self.reset_application()

    def reset_application(self):
        requests.post(f"{self._base_url}/tests/reset")