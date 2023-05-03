import pytest

from api.api_pages.users import UserPage
from api.Schemas.user_schemas import user_single_schema
from api.Schemas.user_schemas import single_user_not_found_schema

class TestUserApiPage:

    @pytest.mark.parametrize("user_id, expected_result, valid_schema", [(2, 200, user_single_schema), (23, 404, single_user_not_found_schema)])
    def test_single_user(self, api_test_url, user_id, expected_result, valid_schema):
        api_response = UserPage(url=api_test_url).get_user_single(valid_schema=valid_schema, user_id=user_id)
        assert api_response.status_code == expected_result



