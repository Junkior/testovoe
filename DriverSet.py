from selenium import  webdriver
from selenium.webdriver.chrome.options import Options

class ChromeDriverSet:
    @staticmethod
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

