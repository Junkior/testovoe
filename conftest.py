import pytest
from selenium import  webdriver
from selenium.webdriver.chrome.options import Options
from faker import Faker
fake = Faker()

@pytest.fixture
def get_chrome_set():
    options = Options()
    path = 'C:/chromedriver.exe'
    options.add_experimental_option('detach', True)
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options, executable_path=path)
    driver.implicitly_wait(10)
    return driver


@pytest.fixture
def data_for_create_user():
    name = fake.name()
    job = fake.job()
    return {"name": name, "job": job}

@pytest.fixture
def data_for_register_user():
    email = fake.email()
    password = fake.password()
    return {"email": email, "password": password}