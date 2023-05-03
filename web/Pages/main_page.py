from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from web.locators import Locators


class MainPage:
        def __init__(self, driver, url):
            self.driver = driver
            self.url = url


        def get_main_page(self):
            self.driver.get(f"{self.url}")

        def click_get_list_users(self):
            self.driver.find_element(*Locators.get_list_users_locator).click()

        def click_get_single_user(self):
            self.driver.find_element(*Locators.get_single_user_locator).click()

        def scroll_to_requests(self):
            self.driver.execute_script("window.scrollBy(0, 1000);")

        def get_response_code(self):
           response_code = self.driver.find_element(*Locators.response_code_locator).text
           return int(response_code)

        def get_response_body(self):
            response_body = self.driver.find_element(*Locators.response_body_locator).text
            return response_body

        def click_single_user_not_found(self):
            self.driver.find_element(*Locators.single_user_not_found_locator).click()

        def click_get_list_resource(self):
            self.driver.find_element(*Locators.unknown_list_locator).click()

        def click_get_single_resource(self):
            self.driver.find_element(*Locators.unknown_single_locator).click()

        def click_single_resource_not_found(self):
            self.driver.find_element(*Locators.unknown_not_found_locator).click()

        def click_create_user(self):
            self.driver.find_element(*Locators.user_create_locator).click()

        def click_fully_update_user(self):
            self.driver.find_element(*Locators.user_put_update_locator).click()

        def click_update_user(self):
            self.driver.find_element(*Locators.user_patch_update_locator).click()

        def click_delete_user(self):
            self.driver.find_element(*Locators.user_delete_locator).click()

        def click_delay_user(self):
            self.driver.find_element(*Locators.user_delay_locator).click()

        def click_register_user_success(self):
            self.driver.find_element(*Locators.register_successful_locator).click()

        def click_register_user_unsuccess(self):
            self.driver.find_element(*Locators.register_unsuccessful_locator).click()

        def click_login_user_success(self):
            self.driver.find_element(*Locators.login_successful_locator).click()

        def click_login_user_unsuccess(self):
            self.driver.find_element(*Locators.login_unsuccessful_locator).click()
