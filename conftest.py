import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from faker import Faker

fake = Faker()


@pytest.fixture
def get_chrome_set():
    options = Options()
    path = 'C:/chromedriver.exe'
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options, executable_path=path)
    driver.implicitly_wait(10)
    return driver


@pytest.fixture
def data_for_create_user():
    body = {"name": "morpheus", "job": "leader"}
    return body


# @pytest.fixture
# def data_for_register_user(request):
#     request.cls.body_positive = {"email": "eve.holt@reqres.in", "password": "pistol"}
#     request.cls.body_negative = {"email": "sydney@fife"}
#
#
# @pytest.fixture(params=[{"email": "eve.holt@reqres.in", "password": "pistol"}])
# def data_for_register_positive(request):
#     return json.dumps(request.param)
#
#
# @pytest.fixture(params=[{"email": "sydney@fife"}])
# def data_for_register_negative(request):
#     return json.dumps(request.param)



@pytest.fixture
def api_test_url(request):
    request.cls.url = 'https://reqres.in/api'


@pytest.fixture
def data_for_update_user():
    body = {"name": "morpheus", "job": "zion resident"}
    return body
