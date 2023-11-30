'''robot-testeissä tarvittava moduli'''
import requests

class Library:
    '''luokka, joka antaa robot-testeissä tarvittavat asetukset'''
    def __init__(self):
        self._base_url = "http://localhost:5000"
        self.reset_application()

    def reset_application(self):
        requests.post(f"{self._base_url}/tests/reset", timeout=5)
