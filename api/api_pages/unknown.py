import requests
from jsonschema import validate


class UnknownPage:
    def __init__(self, url):
        self.url = url

    UNKNOWN_PATH = '/unknown'

    def get_unknown_list(self, valid_schema: dict):
        response = requests.get(f"{self.url}{self.UNKNOWN_PATH}")
        validate(instance=response.json(), schema=valid_schema)
        return response

    def get_unknown_single(self, valid_schema: dict, resource_id):
        response = requests.get(f"{self.url}{self.UNKNOWN_PATH}/{resource_id}")
        validate(instance=response.json(), schema=valid_schema)
        return response


