import time
import json
from api.api_pages.users import UserPage
from web.Pages.main_page import MainPage
from api.Schemas.user_schemas import user_list_schema
from api.Schemas.user_schemas import create_user_schema
API_URL = 'https://reqres.in/api'
WEB_URL = 'https://reqres.in'


def test_list_users(get_chrome_set):
    api_response = UserPage(url=API_URL).get_users_list(valid_schema=user_list_schema)
    api_response_code = api_response.status_code
    api_response_body = json.dumps(api_response.json(), indent=4)
    web_driver = MainPage(driver=get_chrome_set, url=WEB_URL)
    web_driver.get_main_page()
    web_driver.click_get_list_users()
    web_response_code = web_driver.get_response_code()
    web_response_body = web_driver.get_response_body()
    assert api_response_code == web_response_code
    assert api_response_body == web_response_body

def test_api(data_for_create_user):
    api_response = UserPage(url=API_URL).create_user(valid_schema=create_user_schema, body=data_for_create_user)
    status_code = api_response.status_code
    assert status_code == 201