import requests
from jsonschema import validate


class UserPage:
    def __init__(self, url):
        self.url = url

    USERS_PATH = '/users'

    def get_users_list(self, valid_schema: dict, page=2):
        response = requests.get(f"{self.url}{self.USERS_PATH}?page={page}")
        validate(instance=response.json(), schema=valid_schema)
        return response

    def get_user_single(self, valid_schema: dict, user_id=2):
        response = requests.get(f"{self.url}{self.USERS_PATH}/{user_id}")
        validate(instance=response.json(), schema=valid_schema)
        return response

    def create_user(self, valid_schema: dict, body: dict):
        response = requests.post(f"{self.url}{self.USERS_PATH}", json=body)
        validate(instance=response.json(), schema=valid_schema)
        return response

    def fully_update_user(self, valid_schema: dict, user_id, body: dict):
        response = requests.put(f"{self.url}{self.USERS_PATH}/{user_id}", json=body)
        validate(instance=response.json(), schema=valid_schema)
        return response

    def update_user(self, valid_schema: dict, user_id, body:dict):
        response = requests.patch(f"{self.url}{self.USERS_PATH}/{user_id}", json=body)
        validate(instance=response.json(), schema=valid_schema)
        return response

    def delete_user(self, user_id):
        response = requests.delete(f"{self.url}{self.USERS_PATH}/{user_id}")
        return response

    def get_delayed_response(self, valid_schema: dict, delay):
        response = requests.get(f"{self.url}{self.USERS_PATH}?delay={delay}")
        validate(instance=response.json(), schema=valid_schema)
        return response










