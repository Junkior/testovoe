import time
import pytest
import json
from web.Pages.main_page import MainPage
from api.api_pages.users import UserPage
from api.api_pages.unknown import UnknownPage
from api.api_pages.register import RegisterPage
from api.api_pages.login import LoginPage
from api.Schemas import user_schemas
from api.Schemas import unknown_schemas
from api.Schemas import register_schemas
from api.Schemas import login_schemas


@pytest.mark.usefixtures("get_chrome_set", "web_test_url", "api_test_url")
class TestWeb:

    def test_get_list_users(self):
        main_page = MainPage(driver=self.driver, url=self.web_url)
        main_page.get_main_page()
        main_page.click_get_list_users()
        web_response_code = main_page.get_response_code()
        web_json = main_page.get_response_body()
        api_response = UserPage(url=self.url).get_users_list(valid_schema=user_schemas.user_list_schema)
        api_response_code = api_response.status_code
        body = json.dumps(api_response.json(), indent=4)
        assert web_response_code == api_response_code
        assert web_json == body


    @pytest.mark.parametrize(
        "func_name, user_id, valid_schema",
        [("click_get_single_user", 2,
         user_schemas.user_single_schema),
         ("click_single_user_not_found", 23, user_schemas.single_user_not_found_schema)])
    def test_get_single_users(self, func_name, user_id, valid_schema):
        main_page = MainPage(driver=self.driver, url=self.web_url)
        main_page.get_main_page()
        func = getattr(main_page, func_name)
        func()
        response_code = main_page.get_response_code()
        web_body = main_page.get_response_body()
        api_response = UserPage(self.url).get_user_single(valid_schema=valid_schema, user_id=user_id)
        assert json.dumps(api_response.json(), indent=4) == web_body
        assert api_response.status_code == response_code

    def test_create_user(self, data_for_create_user):
        main_page = MainPage(driver=self.driver, url=self.web_url)
        main_page.get_main_page()
        main_page.click_create_user()
        code = main_page.get_response_code()
        api_response = UserPage(self.url).create_user(valid_schema=user_schemas.create_user_schema, body=data_for_create_user)
        # Не сравнить тело ответа от api и тело ответа в Web, т.к. по запросу API возвращает рандомный id каждый раз
        # Так же есть разница в миллисекундах для createdAt
        assert api_response.status_code == code

    def test_put_update_user(self, data_for_update_user):
        main_page = MainPage(driver=self.driver, url=self.web_url)
        main_page.get_main_page()
        main_page.click_fully_update_user()
        code = main_page.get_response_code()
        api_response = UserPage(url=self.url).fully_update_user(valid_schema=user_schemas.update_user_schema,
                                                                body=data_for_update_user)
        assert api_response.status_code == code
        # Не сравнить тело ответа от api и тело ответа в Web из-за разницы в updatedAt

    def test_patch_update_user(self, data_for_update_user):
        main_page = MainPage(driver=self.driver, url=self.web_url)
        main_page.get_main_page()
        main_page.click_update_user()
        code = main_page.get_response_code()
        api_response = UserPage(url=self.url).update_user(valid_schema=user_schemas.update_user_schema,
                                                          body=data_for_update_user)
        assert api_response.status_code == code
        # Не сравнить тело ответа от api и тело ответа в Web из-за разницы в updatedAt


    def test_delete_user(self):
        main_page = MainPage(driver=self.driver, url=self.web_url)
        main_page.get_main_page()
        main_page.click_delete_user()
        code = main_page.get_response_code()
        api_response = UserPage(url=self.url).delete_user()
        assert api_response.status_code == code

    def test_user_delay_response(self):
        main_page = MainPage(driver=self.driver, url=self.web_url)
        main_page.get_main_page()
        main_page.click_delay_user()
        time.sleep(4)
        body = main_page.get_response_body()
        code = main_page.get_response_code()
        api_response = UserPage(url=self.url).get_delayed_response(valid_schema=user_schemas.user_list_schema)
        assert json.dumps(api_response.json(), indent=4) == body
        assert api_response.status_code == code

    def test_get_list_resource(self):
        main_page = MainPage(driver=self.driver, url=self.web_url)
        main_page.get_main_page()
        main_page.click_get_list_resource()
        body = main_page.get_response_body()
        code = main_page.get_response_code()
        api_response = UnknownPage(url=self.url).get_unknown_list(valid_schema=unknown_schemas.unknown_list_schema)
        assert json.dumps(api_response.json(), indent=4) == body
        assert api_response.status_code == code

    @pytest.mark.parametrize(
        "func_name, resource_id, valid_schema",
        [("click_get_single_resource", 2,
          unknown_schemas.unknown_single_schema),
         ("click_single_resource_not_found", 23, unknown_schemas.unknown_single_not_found)])
    def test_get_single_resource(self, func_name, resource_id, valid_schema):
        main_page = MainPage(driver=self.driver, url=self.web_url)
        main_page.get_main_page()
        func = getattr(main_page, func_name)
        func()
        body = main_page.get_response_body()
        code = main_page.get_response_code()
        api_response = UnknownPage(url=self.url).get_unknown_single(valid_schema=valid_schema, resource_id=resource_id)
        assert json.dumps(api_response.json(), indent=4) == body
        assert api_response.status_code == code

    @pytest.mark.parametrize(
        "func_name, json_body, valid_schema",
        [("click_register_user_success",
        {"email": "eve.holt@reqres.in", "password": "pistol"},
          register_schemas.successful_register_schema),
         ("click_register_user_unsuccess", {"email": "sydney@fife"},
          register_schemas.unsuccessful_register_schema)])
    def test_register(self, func_name, json_body, valid_schema):
        main_page = MainPage(driver=self.driver, url=self.web_url)
        main_page.get_main_page()
        func = getattr(main_page, func_name)
        func()
        body = main_page.get_response_body()
        code = main_page.get_response_code()
        api_response = RegisterPage(url=self.url).register_user(valid_schema=valid_schema, body=json_body)
        assert json.dumps(api_response.json(), indent=4) == body
        assert api_response.status_code == code

    @pytest.mark.parametrize(
        "func_name, json_body, valid_schema",
        [("click_login_user_success",
        {"email": "eve.holt@reqres.in","password": "cityslicka"},
          login_schemas.successful_login_schema),
         ("click_login_user_unsuccess",
          {"email": "peter@klaven"},
          login_schemas.unsuccessful_login_schema)])
    def test_login_user(self, func_name, json_body, valid_schema):
        main_page = MainPage(driver=self.driver, url=self.web_url)
        main_page.get_main_page()
        func = getattr(main_page, func_name)
        func()
        body = main_page.get_response_body()
        code = main_page.get_response_code()
        api_response = LoginPage(url=self.url).login_user(valid_schema=valid_schema, body=json_body)
        assert json.dumps(api_response.json(), indent=4) == body
        assert api_response.status_code == code










