import requests
from jsonschema import validate


class RegisterPage:
    def __init__(self, url):\
        self.url = url

    REGISTER_PATH = '/register'

    def register_user(self, valid_schema: dict, body: dict):
        response = requests.post(f"{self.url}{self.REGISTER_PATH}", json=body)
        validate(instance=response.json(), schema=valid_schema)
        return response
