from selenium.webdriver.common.by import By
from base.base_class import Base


class LoginPage(Base):
    # PAGE URL
    URL = 'https://www.saucedemo.com/'

    # Locators
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')

    # Getters
    def get_username_field(self):
        return self.wait_for_element_is_clickable(self.USERNAME_FIELD)

    def get_password_field(self):
        return self.wait_for_element_is_clickable(self.PASSWORD_FIELD)

    def get_login_button(self):
        return self.wait_for_element_is_clickable(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.wait_for_element_is_visible(self.ERROR_MESSAGE)

    # Actions
    def fill_username_field(self, username):
        self.get_username_field().send_keys(username)

    def fill_password_field(self, password):
        self.get_password_field().send_keys(password)

    def click_on_login_button(self):
        self.get_login_button().click()

    # Methods
    def open_login_page(self):
        self.driver.get(self.URL)

    def fill_fields_and_click_on_login_button(self, username, password):
        self.fill_username_field(username)
        self.fill_password_field(password)
        self.click_on_login_button()

    def check_error_message_is_correct(self, expected_error_text):
        self.assert_element_text_value(self.get_error_message(), expected_error_text)
