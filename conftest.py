import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def get_chrome_set(request):
    options = Options()
    path = 'C:/chromedriver.exe'
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options, executable_path=path)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture
def data_for_create_user():
    body = {"name": "morpheus", "job": "leader"}
    return body


@pytest.fixture
def api_test_url(request):
    request.cls.url = 'https://reqres.in/api'


@pytest.fixture
def web_test_url(request):
    request.cls.web_url = 'https://reqres.in'


@pytest.fixture
def data_for_update_user():
    body = {"name": "morpheus", "job": "zion resident"}
    return body
