import pytest

from api.api_pages.users import UserPage
from api.Schemas import user_schemas
from datetime import timedelta


@pytest.mark.usefixtures("api_test_url")
class TestUserApiPage:
    @pytest.mark.parametrize("user_id, expected_result, valid_schema", [(2, 200, user_schemas.user_single_schema), (23, 404, user_schemas.single_user_not_found_schema)])
    def test_single_user(self, user_id, expected_result, valid_schema):
        api_response = UserPage(url=self.url).get_user_single(valid_schema=valid_schema, user_id=user_id)
        assert api_response.status_code == expected_result

    def test_list_users(self):
        api_response = UserPage(url=self.url).get_users_list(valid_schema=user_schemas.user_list_schema)
        assert api_response.status_code == 200


    def test_create_user(self, data_for_create_user):
        api_response = UserPage(url=self.url).create_user(valid_schema=user_schemas.create_user_schema, body=data_for_create_user)
        assert api_response.status_code == 201

    def test_put_update_user(self, data_for_update_user):
        api_response = UserPage(url=self.url).fully_update_user(valid_schema=user_schemas.update_user_schema, body=data_for_update_user)
        assert api_response.status_code == 200

    def test_patch_update_user(self, data_for_update_user):
        api_response = UserPage(url=self.url).update_user(valid_schema=user_schemas.update_user_schema, body=data_for_update_user)
        assert api_response.status_code == 200

    def test_delete_user(self):
        api_response = UserPage(url=self.url).delete_user()
        assert api_response.status_code == 204

    @pytest.mark.parametrize("delay", [(3), (4)])
    def test_user_delay_response(self, delay):
        api_response = UserPage(url=self.url).get_delayed_response(valid_schema=user_schemas.user_list_schema, delay=delay)
        assert api_response.status_code == 200
        assert api_response.elapsed.seconds == delay

# @pytest.mark.usefixtures("api_test_url")
# class TestUnknownApiPage:




