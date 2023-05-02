import requests
from jsonschema import validate


class LoginPage:
    def __init__(self, url):
        self.url = url

    LOGIN_PATH = '/login'

    def login_user(self, valid_schema: dict, body: dict):
        response = requests.post(f"{self.url}{self.LOGIN_PATH}", json=body)
        validate(instance=response.json(), schema=valid_schema)
        return response


