from selenium.webdriver.common.by import By

class Locators(object):
    """Request buttons"""
    get_list_users_locator = (By.CSS_SELECTOR, "[data-id='users']")
    get_single_user_locator = (By.CSS_SELECTOR, "[data-id='users-single']")
    single_user_not_found_locator = (By.CSS_SELECTOR, "[href='/api/users/23'][data-key='try-link']")
    unknown_list_locator = (By.CSS_SELECTOR, "[href='/api/unknown'][data-key='try-link']")
    unknown_single_locator = (By.CSS_SELECTOR, "[href='/api/unknown/2'][data-key='try-link']")
    unknown_not_found_locator = (By.CSS_SELECTOR, "[href='/api/unknown/23'][data-key='try-link']")
    user_create_locator = (By.CSS_SELECTOR, "[data-id='post']")
    user_put_update_locator = (By.CSS_SELECTOR, "[data-id='put']")
    user_patch_update_locator = (By.CSS_SELECTOR, "[data-id='patch'] > [data-key='try-link']")
    user_delete_locator = (By.CSS_SELECTOR, "[data-id='delete']")
    register_successful_locator = (By.CSS_SELECTOR, "[data-id='register-successful'] > [data-key='try-link']")
    register_unsuccessful_locator = (By.CSS_SELECTOR, "[data-id='register-unsuccessful'] > [data-key='try-link']")
    login_successful_locator = (By.CSS_SELECTOR, "[data-id='login-successful'] > [data-key='try-link']")
    login_unsuccessful_locator = (By.CSS_SELECTOR, "[data-id='login-unsuccessful'] > [data-key='try-link']")
    user_delay_locator = (By.CSS_SELECTOR, "[data-id='delay'] > [data-key='try-link']")

    """Response code and response body"""

    response_code_locator = (By.CSS_SELECTOR, ".response-code")
    response_body_locator = (By.CSS_SELECTOR, "[data-key='output-response']")



